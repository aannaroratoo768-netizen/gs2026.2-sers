def analisar_energia(kwh_atual: float, tarifa: float = 0.85) -> dict:
  """Calcula custos atuais e compara eficiência energética vs.

  energia solar por assinatura.
  """
  custo_atual_mensal = kwh_atual * tarifa

  # Alternativa 1: Eficiência Energética (estimativa de 35% de redução no consumo)
  kwh_eficiente = kwh_atual * 0.65
  custo_eficiente_mensal = kwh_eficiente * tarifa
  economia_eficiente = custo_atual_mensal - custo_eficiente_mensal

  # Alternativa 2: Energia Solar por Assinatura (desconto médio de 15% sobre a energia compensada)
  desconto_solar = 0.15
  economia_solar = custo_atual_mensal * desconto_solar
  custo_solar_mensal = custo_atual_mensal - economia_solar

  # Impacto ambiental (Fator médio SIN Brasil ~ 0.0385 kg CO2 / kWh - referência MCTI)
  co2_evitado_eficiencia_anual = (kwh_atual - kwh_eficiente) * 12 * 0.0385
  co2_evitado_solar_anual = kwh_atual * 12 * 0.0385

  return {
      "custo_atual": round(custo_atual_mensal, 2),
      "alternativa_eficiencia": {
          "novo_custo": round(custo_eficiente_mensal, 2),
          "economia_mensal": round(economia_eficiente, 2),
          "co2_evitado_kg_ano": round(co2_evitado_eficiencia_anual, 2),
          "limitacao": (
              "Exige investimento inicial na troca de eletrodomésticos por selo"
              " PROCEL A."
          ),
      },
      "alternativa_solar_assinatura": {
          "novo_custo": round(custo_solar_mensal, 2),
          "economia_mensal": round(economia_solar, 2),
          "co2_evitado_kg_ano": round(co2_evitado_solar_anual, 2),
          "limitacao": (
              "Não reduz o consumo físico de kWh; depende de disponibilidade na"
              " distribuidora local."
          ),
      },
      "referencias": [
          "Tabela PBE/PROCEL - INMETRO",
          "ANEEL - Tarifas Residenciais e Geração Compartilhada (Lei 14.300)",
          "MCTI - Fatores de Emissão de CO2",
      ],
  }


# Exemplo de integração com a resposta do assistente
resultado = analisar_energia(kwh_atual=137.5)
print(resultado)
