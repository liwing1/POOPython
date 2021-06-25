# Desafio POO equipe UnBeatables

O desafio se baseia numa simulação muito simples do jogo.
Vocês devem baixar os arquivos que estão aqui https://drive.google.com/drive/folders/1DDiF5AOOi9ABxktM2gTYNKVY2H76sLqO?usp=sharing .

Atenção: Usar python2! Infelizmente a gente ainda está preso a ele por causa de bibliotecas. 

Usando as classes que estão nos arquivos dentro da pasta Classes, vcs devem implementar um robô de vcs usando como base a classe BaseRobot. 
Eu dou um exemplo com a classe MyRobot, sendo que nela, eu implementei uma andada aleatória e que ele fique gritando no game_stopped :p.

A ideia é implementar o game_stopped e o game_playing nas classes filhas. Se vcs acharem muito fácil, podem implementar o kick_ball também (eu já comecei implementar um algoritmo de rolagem da bola na sua classe). Além disso, seria interessante vcs implementarem um jeito de rodar 5 ou 10 robos ao mesmo tempo, fazendo valer a pena todo o trabalho de construir classes.

O jogo se dá chamando 3 segundos de game_stopped para todos os robos e depois game_playing. Fiz isso pq lembra um pouco mais como é o código competição.
É possível que haja bugs no código, se tiver, vcs podem tentar corrigir eles ou então dá um toque que eu corrijo.

OBS: no main.py, tem uma implementação de leitura do keyboard. Eu pus ela lá para quem quiser usar algum comando de teclado para fazer alguma coisa no programa. Não é necessário usar.

	OBS2: Devido à leitura de teclado ali de cima usar threading, para matar o programa, usem ctrl+\ (barra pra trás mesmo). Isso faz com que todo o programa morra imediatamente. Ctrl+C nao vai matar ele. Outro jeito é matar o processo do programa. ou entao dar Ctrl+Z e dps no mesmo terminal escrever kill %(numero que aparece no terminal), ex: Ctrl+Z, kill %1
