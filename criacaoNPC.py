from random import randint

lista_NPC = []

def criar_NPC():
  level = randint(0,50)
  novo_npc = {
    'Nome': f'Monstro #{level}',
    'Level': f'{level}',
    'HP': 100 * level,
    'Dano': 10 * level,
  }
  lista_NPC.append(novo_npc)


def criar_NPCS(n_NPCS):
  for _ in range(n_NPCS):
    criar_NPC()


def exibir_NPCS():
  for npc in lista_NPC:
    print(
      f"Nome:{npc['Nome']} //"
      f"Level: {npc['Level']} //"
      f"HP: {npc['HP']} //"
      f"Dano: {npc['Dano']}"
  )

criar_NPCS(5)
exibir_NPCS()
