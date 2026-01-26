import os
import pandas as pd
import re
from urllib.parse import urlparse

class ExtractorFeatures:
    """
    Extrai features (características) de URLs para detecção de phishing.
    """

    # Palavras comumente usadas em URLs de phishing
    PALAVRAS_SUSPEITAS = [
    'login', 'verify', 'account', 'update', 'confirm', 'secure',
    'authenticate', 'validate', 'password', 'reset', 'suspended',
    'urgent', 'action', 'click', 'alert', 'warning', 'expire'
]

    # TLDs (extensões) mais comuns em phishing
    TLDS_SUSPEITOS = ['ru', 'tk', 'ml', 'ga', 'cf', 'xyz', 'top', 'gq']

    def __init__(self):
        pass

    def extrair_features(self, url: str) -> dict:
        """
        Extrai todas as features de uma URL.

        Args:
            url (str): URL a analisar

        Returns:
            dict: Dicionário com todas as features
        """
        features = {}

        # 1. FEATURES DE COMPRIMENTO E ESTRUTURA
        features['comprimento_url'] = len(url)
        features['num_pontos'] = url.count('.')
        features['num_barras'] = url.count('/')
        features['num_hifen'] = url.count('-')
        features['num_underline'] = url.count('_')
        features['num_arroba'] = url.count('@')

        # 2. FEATURES DE PROTOCOLO E SEGURANÇA
        features['tem_https'] = 1 if url.startswith('https') else 0
        features['tem_www'] = 1 if 'www' in url else 0
        features['tem_ip'] = 1 if self._tem_ip(url) else 0

        # 3. FEATURES DE DOMÍNIO
        try:
            parsed = urlparse(url)
            dominio = parsed.netloc
            features['num_subdomios'] = dominio.count('.') - 1 if '.' in dominio else 0
            features['comprimento_dominio'] = len(dominio)

            # Extrair TLD
            if '.' in dominio:
                tld = dominio.split('.')[-1]
                features['tld_suspeito'] = 1 if tld.lower() in self.TLDS_SUSPEITOS else 0
            else:
                features['tld_suspeito'] = 0
        except:
            features['num_subdomios'] = 0
            features['comprimento_dominio'] = 0
            features['tld_suspeito'] = 0

        # 4. FEATURES DE PALAVRAS SUSPEITAS
        url_lower = url.lower()
        palavras_encontradas = [p for p in self.PALAVRAS_SUSPEITAS if p in url_lower]
        features['tem_palavras_suspeitas'] = 1 if len(palavras_encontradas) > 0 else 0
        features['num_palavras_suspeitas'] = len(palavras_encontradas)

        # 5. FEATURES DE CARACTERES ESPECIAIS
        features['num_caracteres_especiais'] = len(re.findall(r'[!@#$%^&*()_+=|$$|{};:\'",.<>?/\\|`~]', url))

        # 6. FEATURES DE NÚMEROS
        features['num_digitos'] = len(re.findall(r'\d', url))

        return features

    def _tem_ip(self, url: str) -> bool:
        """
        Verifica se a URL contém um endereço IP.
        """
        # Padrão simples de IP (não é perfeito, mas funciona pra maioria dos casos)
        padrao_ip = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
        return bool(re.search(padrao_ip, url))


def processar_dataset(caminho_entrada: str, caminho_saida: str) -> None:
    """
    Processa o dataset completo, extraindo features de cada URL.

    Args:
        caminho_entrada (str): Caminho do arquivo com URLs preparadas
        caminho_saida (str): Caminho onde salvar o dataset com features
    """
    print("=" * 70)
    print("🔍 EXTRAÇÃO DE FEATURES DE URLs")
    print("=" * 70)

    # Carregar dataset preparado
    if not os.path.exists(caminho_entrada):
        raise FileNotFoundError(f"❌ Arquivo não encontrado: {caminho_entrada}")

    print(f"\n📥 Carregando dataset de: {caminho_entrada}")
    df = pd.read_csv(caminho_entrada)
    print(f"✅ Dataset carregado com {len(df):,} URLs")

    # Inicializar extrator
    extrator = ExtractorFeatures()

    # Extrair features para cada URL
    print("\n🔄 Extraindo features de cada URL...")
    print("   (isso pode levar alguns segundos...)\n")

    lista_features = []

    for idx, row in df.iterrows():
        url = row['url']
        label = row['label']
        label_text = row['label_text']

        # Extrair features
        features = extrator.extrair_features(url)

        # Adicionar URL e label
        features['url'] = url
        features['label_text'] = label_text
        features['label'] = label

        lista_features.append(features)

        # Mostrar progresso a cada 50k URLs
        if (idx + 1) % 50000 == 0:
            print(f"   ✓ {idx + 1:,} URLs processadas...")

    # Criar DataFrame com features
    df_features = pd.DataFrame(lista_features)

    print(f"\n✅ Features extraídas com sucesso!")
    print(f"   Total de features por URL: {len(df_features.columns) - 3}")  # -3 (url, label_text, label)

    # Mostrar estatísticas
    print("\n📊 Estatísticas das features:")
    print(f"\n   Colunas criadas:")
    for col in df_features.columns:
        if col not in ['url', 'label_text', 'label']:
            print(f"      - {col}")

    print(f"\n   Exemplo de uma linha:")
    print(df_features.iloc[0])

    # Salvar dataset com features
    pasta = os.path.dirname(caminho_saida)
    if pasta and not os.path.exists(pasta):
        os.makedirs(pasta, exist_ok=True)

    df_features.to_csv(caminho_saida, index=False, encoding='utf-8')
    print(f"\n💾 Dataset com features salvo em: {caminho_saida}")
    print(f"   Tamanho: {len(df_features):,} linhas x {len(df_features.columns)} colunas")
    print(f"   Arquivo: {os.path.getsize(caminho_saida) / (1024*1024):.2f} MB")

    # Resumo de distribuição
    print(f"\n📈 Distribuição de labels:")
    print(f"   URLs legítimas (good): {(df_features['label'] == 0).sum():,}")
    print(f"   URLs phishing (bad):   {(df_features['label'] == 1).sum():,}")

    print("\n" + "=" * 70)
    print("🏁 EXTRAÇÃO CONCLUÍDA COM SUCESSO!")
    print("=" * 70)


def main():
    """
    Função principal.
    """
    caminho_entrada = os.path.join("dados", "urls_preparado.csv")
    caminho_saida = os.path.join("dados", "urls_com_features.csv")

    processar_dataset(caminho_entrada, caminho_saida)


if __name__ == "__main__":
    main()
