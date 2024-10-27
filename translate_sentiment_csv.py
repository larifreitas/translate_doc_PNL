import pandas as pd
from googletrans import Translator

df = pd.read_csv('./datasets/sentiment_analysis.csv')

print("DataFrame original\n",df)

translator = Translator(service_urls=['translate.googleapis.com', 'translate.google.com'])

df['Translated_Sentence'] = None
df['Translated_Sentiment'] = None

# traduzindo cada linha
print('Traduzindo ...')
for index, row in df.iterrows():
    sentence = row["Sentence"]
    sentiment = row["Sentiment"]
    
    try:
        # Validação
        if pd.notnull(sentence):
            translated_sentence = translator.translate(sentence, dest="pt").text
            df.at[index, 'Translated_Sentence'] = translated_sentence
        if pd.notnull(sentiment):
            translated_sentiment = translator.translate(sentiment, dest="pt").text
            df.at[index, 'Translated_Sentiment'] = translated_sentiment

    except Exception as e:
        print(f"Erro ao traduzir a linha {index}: {e}")

print("\n\nDataFrame traduzido\n",df)

df.to_csv('./datasets/traduzido_sentiment_analysis.csv', index=False)

# selecina colunas para criar novo df e salvar
df_novo = df[['Translated_Sentence', 'Translated_Sentiment']]
df_novo.to_csv('./datasets/novo_sentiment_analysis.csv', index=False)

print("Tradução concluída e salva!")
