import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import joblib

def carregar_dataset(caminho: str) -> pd.DataFrame:
    """
    Carrega o dataset com features já extraídas.
    """
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"❌ Arquivo não encontrado: {caminho}")

    print(f"📥 Carregando dataset com features de: {caminho}")
    df = pd.read_csv(caminho)
    print(f"✅ Dataset carregado com {len(df):,} linhas e {len(df.columns)} colunas.")
    return df

def preparar_dados(df: pd.DataFrame):
    """
    Separa features (X) e label (y).
    """
    # Features: todas as colunas exceto 'url', 'label_text', 'label'
    features = [col for col in df.columns if col not in ['url', 'label_text', 'label']]

    X = df[features].astype(float)  # Garante que tudo é numérico
    y = df['label']                  # 0 = good, 1 = bad

    print(f"\n📊 Features usadas para treino: {features}")
    print(f"   Total de {len(features)} features.")

    return X, y

def treinar_e_avaliar(X, y):
    """
    Divide em treino/teste, treina RandomForest e avalia.
    """
    print("\nSplitOptions train_test_split...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    print(f"   {len(X_train):,} amostras para treino")
    print(f"   {len(X_test):,} amostras para teste")

    # Instancia e treina o modelo
    print("\n🌲 Treinando RandomForestClassifier...")
    modelo = RandomForestClassifier(
        n_estimators=100,      # número de árvores
        max_depth=10,          # profundidade máxima (evita overfit)
        random_state=42,
        n_jobs=-1              # usa todos os núcleos do processador
    )
    modelo.fit(X_train, y_train)

    # Avaliação
    print("\n📈 Avaliando modelo...")
    y_pred = modelo.predict(X_test)

    print(f"\n✅ Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print("\n📋 Classification Report:")
    print(classification_report(y_test, y_pred, target_names=['Legítima (good)', 'Phishing (bad)']))

    print("\n📊 Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    return modelo

def salvar_modelo(modelo, caminho_saida: str):
    """
    Salva o modelo treinado em disco.
    """
    pasta = os.path.dirname(caminho_saida)
    if pasta and not os.path.exists(pasta):
        os.makedirs(pasta, exist_ok=True)

    joblib.dump(modelo, caminho_saida)
    print(f"\n💾 Modelo salvo em: {caminho_saida}")
    print(f"   Tamanho do arquivo: {os.path.getsize(caminho_saida) / 1024:.2f} KB")

def main():
    """
    Pipeline completo de treino.
    """
    print("=" * 70)
    print("🌲 TREINAMENTO DE MODELO DE DETECÇÃO DE PHISHING")
    print("=" * 70)

    caminho_entrada = os.path.join("dados", "urls_com_features.csv")
    caminho_modelo = os.path.join("modelos", "modelo_phishing.pkl")

    # 1. Carregar dataset com features
    df = carregar_dataset(caminho_entrada)

    # 2. Preparar dados
    X, y = preparar_dados(df)

    # 3. Treinar e avaliar
    modelo = treinar_e_avaliar(X, y)

    # 4. Salvar modelo
    salvar_modelo(modelo, caminho_modelo)

    print("\n" + "=" * 70)
    print("✅ TREINAMENTO CONCLUÍDO COM SUCESSO!")
    print("=" * 70)
    

if __name__ == "__main__":
    main()
