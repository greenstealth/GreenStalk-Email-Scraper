GreenStalk Email Scraper
O GreenStalk Email Scraper é uma ferramenta avançada de raspagem de e-mails projetada para profissionais de segurança, marketing e pesquisa de dados. Utilizando técnicas de OSINT (Open Source Intelligence), esta aplicação é capaz de extrair e-mails de diversas fontes na web de forma eficiente e automatizada.

Características
Raspagem em Massa: Extraia e-mails de múltiplas fontes web simultaneamente, otimizando o processo de coleta de dados.
Filtragem Avançada: Filtre e-mails por domínio específico, permitindo uma coleta de dados direcionada e relevante.
Suporte a Provedores Diversos: Além de e-mails brasileiros (.br), a ferramenta suporta a coleta de e-mails de provedores globais como Gmail, Yahoo, entre outros.
Exportação em CSV: Salve os e-mails raspados em arquivos CSV para fácil análise e integração com outras ferramentas.
Interface Simples: Operação simplificada via terminal, tornando a ferramenta acessível para usuários de todos os níveis técnicos.
Compatível com Kali Linux: Desenvolvido e testado para operação eficiente em ambientes Kali Linux.
Utilização
Ideal para profissionais de segurança cibernética, marketing digital, e pesquisadores que necessitam de uma ferramenta robusta para coleta de e-mails para análise, campanhas de marketing, ou atividades de pentesting e OSINT.

Instalação e Uso
Para usar este sistema, você precisará de Python instalado em seu ambiente. Este sistema foi testado no ambiente Kali Linux.

Clone o repositório:

bash
Copy code
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Instale as dependências:
Utilize o comando abaixo para instalar as dependências necessárias.

bash
Copy code
pip install -r requirements.txt
Uso
Para usar o sistema, siga os passos abaixo:

Execute o script principal:

bash
Copy code
python main.py
Siga as instruções no menu:
O sistema oferece um menu de opções para escolher o tipo de raspagem de e-mails que deseja realizar. Escolha uma das opções fornecidas e siga as instruções na tela.

Opções de Raspagem
Raspagem de e-mails brasileiros: Escolha esta opção para coletar e-mails com domínios brasileiros (terminados em .br).

Raspagem de e-mails do Gmail: Escolha esta opção para coletar e-mails do provedor Gmail.

Raspagem em massa de um arquivo de URLs: Escolha esta opção para realizar a raspagem em massa a partir de uma lista de URLs fornecida em um arquivo de texto.

Arquivos do Projeto
main.py: Script principal que executa o programa.
email_scraper.py: Contém a lógica para fazer a raspagem de e-mails nas páginas web.
email_filter.py: Contém a função para filtrar e-mails de acordo com o domínio.
email_saver.py: Contém a função para salvar os e-mails coletados em um arquivo CSV.
requirements.txt: Lista as dependências necessárias para executar o sistema.
Contribuições
Contribuições para o projeto são bem-vindas. Sinta-se livre para clonar, usar e modificar o código conforme necessário.
