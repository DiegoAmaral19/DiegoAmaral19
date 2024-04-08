{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMdw8gMGrduahNjuXhTg0Cx",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/DiegoAmaral19/DiegoAmaral19/blob/main/Challenge.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install --upgrade google-cloud-speech\n",
        "!pip install streamlit\n",
        "!pip install pyngrok  # Instalação do Ngrok"
      ],
      "metadata": {
        "id": "JrUH_noQYgS8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!ngrok authtoken 2endM5zWuCxtl7wvXTZCF7BKU2j_Acu8zcdZ6D8DETUzyqaP\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Qf_gmblhnyHT",
        "outputId": "8e2cfeb1-0702-4186-8b70-0e8a98b43645"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Authtoken saved to configuration file: /root/.config/ngrok/ngrok.yml\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Importando as bibliotecas necessárias\n",
        "import os\n",
        "from google.cloud import speech_v1p1beta1 as speech\n",
        "import streamlit as st\n",
        "from pyngrok import ngrok  # Importação do Ngrok\n",
        "\n",
        "# Configuração do authtoken do Ngrok\n",
        "NGROK_AUTH_TOKEN = \"2endM5zWuCxtl7wvXTZCF7BKU2j_Acu8zcdZ6D8DETUzyqaP\"\n",
        "ngrok.set_auth_token(NGROK_AUTH_TOKEN)\n",
        "\n",
        "# Função para transcrever áudio usando a API do Google Speech-to-Text\n",
        "def transcrever_audio(audio_file):\n",
        "    client = speech.SpeechClient()\n",
        "\n",
        "    with open(audio_file, \"rb\") as f:\n",
        "        content = f.read()\n",
        "\n",
        "    audio = speech.RecognitionAudio(content=content)\n",
        "    config = speech.RecognitionConfig(\n",
        "        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,\n",
        "        language_code=\"pt-BR\",\n",
        "    )\n",
        "\n",
        "    response = client.recognize(config=config, audio=audio)\n",
        "\n",
        "    return response.results[0].alternatives[0].transcript\n",
        "\n",
        "# Função para análise de sentimentos simples\n",
        "def analisar_sentimentos(texto):\n",
        "    # Aqui você pode implementar a análise de sentimentos utilizando NLTK ou spaCy\n",
        "    # Por exemplo, verificar palavras-chave para determinar sentimentos positivos ou negativos\n",
        "    # Retorna um valor de NPS (Net Promoter Score)\n",
        "\n",
        "    # Implementação simplificada apenas para fins de demonstração\n",
        "    if \"bom\" in texto:\n",
        "        return \"Promotor\"\n",
        "    elif \"ruim\" in texto:\n",
        "        return \"Detrator\"\n",
        "    else:\n",
        "        return \"Neutro\"\n",
        "\n",
        "# Interface de Usuário com Streamlit\n",
        "def main():\n",
        "    st.title(\"Transcrição de Áudio e Análise de Sentimentos\")\n",
        "\n",
        "    # Upload de arquivo de áudio\n",
        "    audio_file = st.file_uploader(\"Selecione um arquivo de áudio\", type=[\"mp3\", \"wav\"])\n",
        "\n",
        "    if audio_file is not None:\n",
        "        st.audio(audio_file, format='audio/wav')\n",
        "\n",
        "        # Transcrever áudio\n",
        "        texto_transcrito = transcrever_audio(audio_file)\n",
        "\n",
        "        # Mostrar texto transcrito\n",
        "        st.subheader(\"Texto Transcrito:\")\n",
        "        st.write(texto_transcrito)\n",
        "\n",
        "        # Analisar Sentimentos\n",
        "        sentimento = analisar_sentimentos(texto_transcrito)\n",
        "        st.subheader(\"Análise de Sentimentos:\")\n",
        "        st.write(sentimento)\n",
        "\n",
        "# Executar a interface de usuário\n",
        "if __name__ == \"__main__\":\n",
        "    # Cria um túnel usando o Ngrok\n",
        "    public_url = ngrok.connect(addr='8501')\n",
        "    print('Link do aplicativo:', public_url)\n",
        "\n",
        "    # Inicia a execução do aplicativo Streamlit\n",
        "    main()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Dd-xrDcTYL4y",
        "outputId": "768609a6-6cdf-46bf-ab38-2b78096604ef"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Link do aplicativo: NgrokTunnel: \"https://5b3a-34-73-31-92.ngrok-free.app\" -> \"http://localhost:8501\"\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!streamlit run Challenge.ipynb\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yEfCdu29oMp1",
        "outputId": "0df39cd2-f5bb-4c30-ad09-50889b51976a"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Usage: streamlit run [OPTIONS] TARGET [ARGS]...\n",
            "Try 'streamlit run --help' for help.\n",
            "\n",
            "Error: Streamlit requires raw Python (.py) files, not .ipynb.\n",
            "For more information, please see https://docs.streamlit.io\n"
          ]
        }
      ]
    }
  ]
}
