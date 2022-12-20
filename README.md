# SEL0337   Aplicação de Microprocessadores II

Este repositório foi criado como uma parte da prática 6, da disciplina Aplicação de Microprocessadores II

Nesta prática, iremos estudar a utilização de periféricos, como a camêra, a qual, inicialmente foi conectada no slot com a denominação "câmera", e em seguida habilitamos a conexão I2C, nas configurações da rasp, para se comunicar com a câmera. 

Após esta etapa inicial, importamos os módulos necessário para os códigos em Python, e através de tutoriais, aprendemos a acessar a câmera, e também a obter dados de estações climáticas. Os dados obtidos de clima pode ser observados no arquivo "dados_clima.txt", e como informado ao professor, perdi meu PenDrive e por consequência não possuo mais as fotos, assim como os dados de clima que foram gerados depois da prática.

Neste repositório, estão os códigos utilizados, e os códigos estão comentados, explicando cada etapa do código.
A biblioteca utilizada para acessar a câmera foi a Picamera, a partir da qual defini-se a resolução e o fram rate, e apartir da função .capture, consegue capturar uma foto, ou pode-se utilizar a função .start_recording para começar a gravar um vídeo. 
Já para a parte de obterr dados climáticos, foram utilizadas as bibliotecas request e json, a primeira nos permite a acessar um site e obter dados, e a segunda para ler os dados. Esta parte de obter dados clim´ticos, trabalhamos com API's.
