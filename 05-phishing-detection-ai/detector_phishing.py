import os
import sys
import pandas as pd
import joblib
from urllib.parse import urlparse
import re

# Importar a classe de extração de features
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
from extrair_features import ExtractorFeatures


class DetectorPhishing:
    """
    Detector de phishing em tempo real usando modelo treinado.
    """

    def __init__(self, caminho_modelo: str):
        """
        Carrega o modelo treinado.

        Args:
            caminho_modelo (str): Caminho do arquivo .pkl do modelo
        """
        if not os.path.exists(caminho_modelo):
            raise FileNotFoundError(f"❌ Modelo não encontrado: {caminho_modelo}")

        print(f"📥 Carregando modelo de: {caminho_modelo}")
        self.modelo = joblib.load(caminho_modelo)
        self.extrator = ExtractorFeatures()
        print("✅ Modelo carregado com sucesso!\n")

    def detectar(self, url: str) -> dict:
        """
        Detecta se uma URL é phishing ou legítima.

        Args:
            url (str): URL a analisar

        Returns:
            dict: Resultado com classificação e confiança
        """
        # Extrair features
        features = self.extrator.extrair_features(url)

        # Ordenar features na mesma ordem usada no treino
        nomes_features = [
            'comprimento_url', 'num_pontos', 'num_barras', 'num_hifen',
            'num_underline', 'num_arroba', 'tem_https', 'tem_www', 'tem_ip',
            'num_subdomios', 'comprimento_dominio', 'tld_suspeito',
            'tem_palavras_suspeitas', 'num_palavras_suspeitas',
            'num_caracteres_especiais', 'num_digitos'
        ]

        X = [[features[nome] for nome in nomes_features]]

        # Fazer predição
        predicao = self.modelo.predict(X)[0]
        probabilidades = self.modelo.predict_proba(X)[0]

        # Extrair confiança
        confianca = max(probabilidades) * 100

        resultado = {
            'url': url,
            'classificacao': 'PHISHING 🚨' if predicao == 1 else 'LEGÍTIMA ✅',
            'label_numerico': predicao,
            'confianca': confianca,
            'prob_legit': probabilidades[0] * 100,
            'prob_phishing': probabilidades[1] * 100,
            'features': features
        }

        return resultado

    def mostrar_resultado(self, resultado: dict) -> None:
        """
        Exibe o resultado de forma formatada.
        """
        print("=" * 70)
        print("🔍 RESULTADO DA ANÁLISE")
        print("=" * 70)
        print(f"\n📍 URL: {resultado['url']}")
        print(f"\n🎯 Classificação: {resultado['classificacao']}")
        print(f"   Confiança: {resultado['confianca']:.2f}%")
        print(f"\n📊 Probabilidades:")
        print(f"   Legítima: {resultado['prob_legit']:.2f}%")
        print(f"   Phishing: {resultado['prob_phishing']:.2f}%")
        print("\n📋 Features Analisadas:")
        for feature, valor in resultado['features'].items():
            print(f"   {feature}: {valor}")
        print("\n" + "=" * 70 + "\n")


def main():
    """
    Função principal com interface interativa.
    """
    print("=" * 70)
    print("🌐 DETECTOR DE PHISHING EM TEMPO REAL")
    print("=" * 70 + "\n")

    # Carregar modelo
    caminho_modelo = os.path.join("modelos", "modelo_phishing.pkl")
    detector = DetectorPhishing(caminho_modelo)

    # Interface interativa
    while True:
        print("Opções:")
        print("  1. Testar uma URL")
        print("  2. Testar múltiplas URLs (de um arquivo)")
        print("  3. Sair")

        opcao = input("\nEscolha uma opção (1/2/3): ").strip()

        if opcao == "1":
            url = input("\n🔗 Digite a URL a analisar: ").strip()
            if url:
                resultado = detector.detectar(url)
                detector.mostrar_resultado(resultado)
            else:
                print("❌ URL vazia!\n")

        elif opcao == "2":
            arquivo = input("\n📁 Digite o caminho do arquivo (CSV com coluna 'url'): ").strip()
            if os.path.exists(arquivo):
                df = pd.read_csv(arquivo)
                if 'url' not in df.columns:
                    print("❌ Arquivo deve ter coluna 'url'\n")
                    continue

                resultados = []
                print(f"\n🔄 Analisando {len(df)} URLs...\n")

                for idx, row in df.iterrows():
                    url = row['url']
                    resultado = detector.detectar(url)
                    resultados.append(resultado)

                    if (idx + 1) % 10 == 0:
                        print(f"   ✓ {idx + 1} URLs processadas...")

                # Salvar resultados
                df_resultados = pd.DataFrame([
                    {
                        'url': r['url'],
                        'classificacao': r['classificacao'],
                        'confianca': r['confianca'],
                        'prob_legit': r['prob_legit'],
                        'prob_phishing': r['prob_phishing']
                    }
                    for r in resultados
                ])

                arquivo_saida = "resultados/deteccoes.csv"
                pasta = os.path.dirname(arquivo_saida)
                if not os.path.exists(pasta):
                    os.makedirs(pasta, exist_ok=True)

                df_resultados.to_csv(arquivo_saida, index=False, encoding='utf-8')
                print(f"\n✅ Resultados salvos em: {arquivo_saida}")

                # Estatísticas
                phishing_count = (df_resultados['classificacao'].str.contains('PHISHING')).sum()
                legit_count = len(df_resultados) - phishing_count
                print(f"\n📊 Resumo:")
                print(f"   URLs legítimas: {legit_count}")
                print(f"   URLs phishing: {phishing_count}\n")
            else:
                print(f"❌ Arquivo não encontrado: {arquivo}\n")

        elif opcao == "3":
            print("👋 Até logo!\n")
            break

        else:
            print("❌ Opção inválida!\n")


if __name__ == "__main__":
    main()
