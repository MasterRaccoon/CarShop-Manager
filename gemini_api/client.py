import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def get_car_ai_bio(model, brand, year):
	message = ''''
	Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo.
	Descreva especificações técnicas desse modelo de carro.
	'''
	message = message.format(brand, model, year)
	gemini_model = genai.GenerativeModel("gemini-1.5-flash")
	response = gemini_model.generate_content(message)

	return response.text
