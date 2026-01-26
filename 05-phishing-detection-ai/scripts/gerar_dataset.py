import os
import pandas as pd

def carregar_dataset_bruto(caminho_arquivo: str) -> pd.DataFrame:
    """
    Carrega o dataset bruto de URLs de phishing/legítimas do Kaggle.

    Espera um CSV com colunas 'URL' e 'Label' (good/bad).
    """
    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(f"❌ Arquivo não encontrado: {caminho_arquivo}")

    print(f"📥 Carregando dataset bruto de: {caminho_arquivo}")
    df = pd.read_csv(caminho_arquivo)

    print(f"✅ Dataset carregado com {len(df):,} linhas e {len(df.columns)} colunas.")
    print(f"📋 Colunas encontradas: {list(df.columns)}")
    return df


def padronizar_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Padroniza o dataset:
    - Renomeia 'URL' → 'url'
    - Normaliza 'Label' → 'label_text' (minúsculo)
    - Cria 'label' numérico (0 = good, 1 = bad)
    """
    print("\n🔧 Padronizando dataset...")

    # Criar DataFrame padronizado
    df_pad = pd.DataFrame()

    # Padronizar coluna de URL
    df_pad['url'] = df['URL'].astype(str).str.strip()

    # Normalizar label para minúsculo
    df_pad['label_text'] = df['Label'].astype(str).str.strip().str.lower()

    # Criar label numérico
    # 0 = legítimo (good)
    # 1 = phishing (bad)
    mapa_label = {
        'good': 0,
        'bad': 1
    }

    df_pad['label'] = df_pad['label_text'].map(mapa_label)

    # Verificar se há valores não mapeados
    nao_mapeados = df_pad[df_pad['label'].isna()]['label_text'].unique()
    if len(nao_mapeados) > 0:
        print(f"⚠️  Aviso: encontrados rótulos não mapeados: {nao_mapeados}")
        print("   Essas linhas serão removidas.")
        df_pad = df_pad[~df_pad['label'].isna()]

    df_pad['label'] = df_pad['label'].astype(int)

    # Estatísticas
    print(f"\n📊 Distribuição de labels:")
    print(df_pad['label_text'].value_counts())
    print(f"\n   Total de URLs legítimas (good): {(df_pad['label'] == 0).sum():,}")
    print(f"   Total de URLs phishing (bad):   {(df_pad['label'] == 1).sum():,}")

    print(f"\n✅ Dataset padronizado com {len(df_pad):,} linhas.")
    print("\n📋 Exemplo de linhas:")
    print(df_pad.head(3))

    return df_pad


def salvar_dataset(df: pd.DataFrame, caminho_saida: str) -> None:
    """
    Salva o DataFrame padronizado em CSV.
    """
    pasta = os.path.dirname(caminho_saida)
    if pasta and not os.path.exists(pasta):
        os.makedirs(pasta, exist_ok=True)

    df.to_csv(caminho_saida, index=False, encoding='utf-8')
    print(f"\n💾 Dataset padronizado salvo em: {caminho_saida}")
    print(f"   Tamanho do arquivo: {os.path.getsize(caminho_saida) / (1024*1024):.2f} MB")


def main():
    """
    Função principal: carrega, padroniza e salva o dataset.
    """
    print("=" * 60)
    print("🎣 PREPARAÇÃO DO DATASET DE PHISHING")
    print("=" * 60)

    # Caminhos dos arquivos
    caminho_bruto = os.path.join("dados", "phishing_site_urls_raw.csv")
    caminho_saida = os.path.join("dados", "urls_preparado.csv")

    # Pipeline de preparação
    df_bruto = carregar_dataset_bruto(caminho_bruto)
    df_padronizado = padronizar_dataset(df_bruto)
    salvar_dataset(df_padronizado, caminho_saida)

    print("\n" + "=" * 60)
    print("🏁 PREPARAÇÃO CONCLUÍDA COM SUCESSO!")
    print("=" * 60)
    print(f"\n📁 Próximo passo: usar 'dados/urls_preparado.csv' para:")
    print("   1. Extrair features das URLs")
    print("   2. Treinar modelo de classificação")
    print("   3. Detectar phishing em tempo real")


if __name__ == "__main__":
    main()
