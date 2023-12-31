{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
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
        "<a href=\"https://colab.research.google.com/gist/VictorOlaf/bf2795f7d997df83eba694bb8598bff0/chatbotmixto.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gpz1NXQ1nfoE",
        "outputId": "1a0bf3d4-2a85-4af5-e4e6-f1cff1724370"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: transformers in /usr/local/lib/python3.10/dist-packages (4.35.2)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from transformers) (3.13.1)\n",
            "Requirement already satisfied: huggingface-hub<1.0,>=0.16.4 in /usr/local/lib/python3.10/dist-packages (from transformers) (0.19.4)\n",
            "Requirement already satisfied: numpy>=1.17 in /usr/local/lib/python3.10/dist-packages (from transformers) (1.23.5)\n",
            "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from transformers) (23.2)\n",
            "Requirement already satisfied: pyyaml>=5.1 in /usr/local/lib/python3.10/dist-packages (from transformers) (6.0.1)\n",
            "Requirement already satisfied: regex!=2019.12.17 in /usr/local/lib/python3.10/dist-packages (from transformers) (2023.6.3)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from transformers) (2.31.0)\n",
            "Requirement already satisfied: tokenizers<0.19,>=0.14 in /usr/local/lib/python3.10/dist-packages (from transformers) (0.15.0)\n",
            "Requirement already satisfied: safetensors>=0.3.1 in /usr/local/lib/python3.10/dist-packages (from transformers) (0.4.0)\n",
            "Requirement already satisfied: tqdm>=4.27 in /usr/local/lib/python3.10/dist-packages (from transformers) (4.66.1)\n",
            "Requirement already satisfied: fsspec>=2023.5.0 in /usr/local/lib/python3.10/dist-packages (from huggingface-hub<1.0,>=0.16.4->transformers) (2023.6.0)\n",
            "Requirement already satisfied: typing-extensions>=3.7.4.3 in /usr/local/lib/python3.10/dist-packages (from huggingface-hub<1.0,>=0.16.4->transformers) (4.5.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests->transformers) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests->transformers) (3.4)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests->transformers) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests->transformers) (2023.7.22)\n"
          ]
        }
      ],
      "source": [
        "!pip install transformers"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import json\n",
        "import numpy as np\n",
        "import tensorflow as tf\n",
        "from transformers import TFAutoModelForSequenceClassification, AutoTokenizer,TFAutoModelForQuestionAnswering\n",
        "\n",
        "\n",
        "#Su modelo de Clasificador\n",
        "ruta_del_modelo = 'drive/MyDrive/ChatBot1'\n",
        "tokenizerB = AutoTokenizer.from_pretrained(ruta_del_modelo)\n",
        "model_intenciones = TFAutoModelForSequenceClassification.from_pretrained(ruta_del_modelo)\n",
        "\n",
        "#Su modelo de Question Answering\n",
        "tokenizerA = AutoTokenizer.from_pretrained(\"IIC/roberta-base-spanish-sqac\")\n",
        "model_respuestas = TFAutoModelForQuestionAnswering.from_pretrained(\"IIC/roberta-base-spanish-sqac\")\n",
        "\n",
        "\n",
        "with open(ruta_del_modelo+'/DiccionarioClases.json', 'r') as f:\n",
        "    diccionario_cargado = json.load(f)\n",
        "\n",
        "def predict_intention(text):\n",
        "    inputs = tokenizerB(text, return_tensors=\"tf\")\n",
        "    predictions = model_intenciones(inputs['input_ids'])\n",
        "    print(predictions.logits)\n",
        "    return np.argmax(predictions.logits)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "x8M8hY2ArQkG",
        "outputId": "61a0d153-bdaf-4ba6-c4a5-a512434d4882"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "Some layers from the model checkpoint at drive/MyDrive/ChatBot1 were not used when initializing TFBertForSequenceClassification: ['dropout_75']\n",
            "- This IS expected if you are initializing TFBertForSequenceClassification from the checkpoint of a model trained on another task or with another architecture (e.g. initializing a BertForSequenceClassification model from a BertForPreTraining model).\n",
            "- This IS NOT expected if you are initializing TFBertForSequenceClassification from the checkpoint of a model that you expect to be exactly identical (initializing a BertForSequenceClassification model from a BertForSequenceClassification model).\n",
            "All the layers of TFBertForSequenceClassification were initialized from the model checkpoint at drive/MyDrive/ChatBot1.\n",
            "If your task is similar to the task the model of the checkpoint was trained on, you can already use TFBertForSequenceClassification for predictions without further training.\n",
            "Some weights of the PyTorch model were not used when initializing the TF 2.0 model TFRobertaForQuestionAnswering: ['roberta.embeddings.position_ids']\n",
            "- This IS expected if you are initializing TFRobertaForQuestionAnswering from a PyTorch model trained on another task or with another architecture (e.g. initializing a TFBertForSequenceClassification model from a BertForPreTraining model).\n",
            "- This IS NOT expected if you are initializing TFRobertaForQuestionAnswering from a PyTorch model that you expect to be exactly identical (e.g. initializing a TFBertForSequenceClassification model from a BertForSequenceClassification model).\n",
            "All the weights of TFRobertaForQuestionAnswering were initialized from the PyTorch model.\n",
            "If your task is similar to the task the model of the checkpoint was trained on, you can already use TFRobertaForQuestionAnswering for predictions without further training.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(diccionario_cargado)\n",
        "\n",
        "while True:\n",
        "  pregunta = input(\"Usuario: \")\n",
        "  if pregunta==\"Detener\":\n",
        "    break\n",
        "  intencion = str(predict_intention(pregunta))\n",
        "  #print(f\"Intención detectada: {diccionario_cargado[intencion]}\")\n",
        "\n",
        "  if diccionario_cargado[intencion]==\"Saludo\":\n",
        "    Saludos=[\"Hola\", \"Hi\", \"Que hay\"]\n",
        "    eleccion=np.random.randint(0,len(Saludos))\n",
        "    print(f\"Asistente: {Saludos[eleccion]}\")\n",
        "  elif diccionario_cargado[intencion]==\"Consulta de Precio\":\n",
        "    Contexto=\"un pastel de chocolate cuesta 20 pesos, un pastel de vainilla cuesta 30 pesos y un pastel de  \"\n",
        "    question, text = pregunta, Contexto\n",
        "    inputs = tokenizerA(question, text, return_tensors=\"tf\")\n",
        "    outputs = model_respuestas(inputs)\n",
        "    start_scores = outputs.start_logits\n",
        "    end_scores = outputs.end_logits\n",
        "    start_index = tf.argmax(start_scores, axis=1).numpy()[0]\n",
        "    end_index = tf.argmax(end_scores, axis=1).numpy()[0] + 1\n",
        "\n",
        "    respuesta = tokenizerA.convert_tokens_to_string(tokenizerA.convert_ids_to_tokens(inputs[\"input_ids\"][0, start_index:end_index]))\n",
        "    print(f\"Asistente: {respuesta}\")\n",
        "  elif diccionario_cargado[intencion]==\"Consulta de Envío\":\n",
        "    Contexto=\"El envio dentro de la ciudad de puebla cuesta 50 pesos, si es a otro estado de la republica el envio cuesta 100 pesos\"\n",
        "    question, text = pregunta, Contexto\n",
        "    inputs = tokenizerA(question, text, return_tensors=\"tf\")\n",
        "    outputs = model_respuestas(inputs)\n",
        "    start_scores = outputs.start_logits\n",
        "    end_scores = outputs.end_logits\n",
        "    start_index = tf.argmax(start_scores, axis=1).numpy()[0]\n",
        "    end_index = tf.argmax(end_scores, axis=1).numpy()[0] + 1\n",
        "\n",
        "    respuesta = tokenizerA.convert_tokens_to_string(tokenizerA.convert_ids_to_tokens(inputs[\"input_ids\"][0, start_index:end_index]))\n",
        "    print(f\"Asistente: {respuesta}\")\n",
        "  elif diccionario_cargado[intencion]==\"Despedida\":\n",
        "    marcador=0\n",
        "    pregunta=pregunta.split(\" \")\n",
        "    for palabra in pregunta:\n",
        "      if palabra==\"Pablo\":\n",
        "        marcador=1\n",
        "      elif palabra==\"Pedro\":\n",
        "        marcador=2\n",
        "    if marcador==1:\n",
        "      print(f\"Asistente: Adios Pablo\")\n",
        "    elif marcador==2:\n",
        "      print(f\"Asistente: Adios Pedro\")\n",
        "    else:\n",
        "      print(f\"Asistente: Adios Quien seas\")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 512
        },
        "id": "n5XfgoZNsUIv",
        "outputId": "df6bfbeb-244b-4e26-9cdd-90dff2298401"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'0': 'Consulta de Envío', '1': 'Consulta de Precio', '2': 'Despedida', '3': 'Saludo'}\n",
            "Usuario: Hola\n",
            "tf.Tensor([[-1.1143682  -1.0358889  -0.50473374  0.86460996 -0.36896458]], shape=(1, 5), dtype=float32)\n",
            "Asistente: Hola\n",
            "Usuario: hola\n",
            "tf.Tensor([[-1.1143682  -1.0358889  -0.50473374  0.86460996 -0.36896458]], shape=(1, 5), dtype=float32)\n",
            "Asistente: Hi\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-26-ddbcd52fd4d6>\u001b[0m in \u001b[0;36m<cell line: 3>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mwhile\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m   \u001b[0mpregunta\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Usuario: \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      5\u001b[0m   \u001b[0;32mif\u001b[0m \u001b[0mpregunta\u001b[0m\u001b[0;34m==\u001b[0m\u001b[0;34m\"Detener\"\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m     \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[0;34m(self, prompt)\u001b[0m\n\u001b[1;32m    849\u001b[0m                 \u001b[0;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    850\u001b[0m             )\n\u001b[0;32m--> 851\u001b[0;31m         return self._input_request(str(prompt),\n\u001b[0m\u001b[1;32m    852\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    853\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_header\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m    893\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    894\u001b[0m                 \u001b[0;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 895\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Interrupted by user\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    896\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    897\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Invalid Message:\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
          ]
        }
      ]
    }
  ]
}
