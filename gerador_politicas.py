import tkinter as tk
from datetime import date
import pyperclip


def gerar_politica_texto():
    nome_site = nome_site_entry.get()
    dominio_site = dominio_site_entry.get()
    data_atual = date.today().strftime("%d/%m/%Y")

    politica_text = f"""Política Privacidade

A sua privacidade é importante para nós. É política do {nome_site} respeitar a sua privacidade em relação a qualquer informação sua que possamos coletar no site {dominio_site}, e outros sites que possuímos e operamos.

Solicitamos informações pessoais apenas quando realmente precisamos delas para lhe fornecer um serviço. Fazemo-lo por meios justos e legais, com o seu conhecimento e consentimento. Também informamos por que estamos coletando e como será usado.

Apenas retemos as informações coletadas pelo tempo necessário para fornecer o serviço solicitado. Quando armazenamos dados, protegemos dentro de meios comercialmente aceitáveis ​​para evitar perdas e roubos, bem como acesso, divulgação, cópia, uso ou modificação não autorizados.

Não compartilhamos informações de identificação pessoal publicamente ou com terceiros, exceto quando exigido por lei.

O nosso site pode ter links para sites externos que não são operados por nós. Esteja ciente de que não temos controle sobre o conteúdo e práticas desses sites e não podemos aceitar responsabilidade por suas respectivas políticas de privacidade.

Você é livre para recusar a nossa solicitação de informações pessoais, entendendo que talvez não possamos fornecer alguns dos serviços desejados.

O uso continuado de nosso site será considerado como aceitação de nossas práticas em torno de privacidade e informações pessoais. Se você tiver alguma dúvida sobre como lidamos com dados do usuário e informações pessoais, entre em contato conosco.


O serviço Google AdSense que usamos para veicular publicidade usa um cookie DoubleClick para veicular anúncios mais relevantes em toda a Web e limitar o número de vezes que um determinado anúncio é exibido para você.
Para mais informações sobre o Google AdSense, consulte as FAQs oficiais sobre privacidade do Google AdSense.
Utilizamos anúncios para compensar os custos de funcionamento deste site e fornecer financiamento para futuros desenvolvimentos. Os cookies de publicidade comportamental usados ​​por este site foram projetados para garantir que você forneça os anúncios mais relevantes sempre que possível, rastreando anonimamente seus interesses e apresentando coisas semelhantes que possam ser do seu interesse.
Vários parceiros anunciam em nosso nome e os cookies de rastreamento de afiliados simplesmente nos permitem ver se nossos clientes acessaram o site através de um dos sites de nossos parceiros, para que possamos creditá-los adequadamente e, quando aplicável, permitir que nossos parceiros afiliados ofereçam qualquer promoção que pode fornecê-lo para fazer uma compra.


Compromisso do Usuário
O usuário se compromete a fazer uso adequado dos conteúdos e da informação que o {nome_site} oferece no site e com caráter enunciativo, mas não limitativo:

A) Não se envolver em atividades que sejam ilegais ou contrárias à boa fé a à ordem pública;
B) Não difundir propaganda ou conteúdo de natureza racista, xenofóbica, jogos de azar, qualquer tipo de pornografia ilegal, de apologia ao terrorismo ou contra os direitos humanos;
C) Não causar danos aos sistemas físicos (hardwares) e lógicos (softwares) do {nome_site}, de seus fornecedores ou terceiros, para introduzir ou disseminar vírus informáticos ou quaisquer outros sistemas de hardware ou software que sejam capazes de causar danos anteriormente mencionados.
Mais informações
Esperemos que esteja esclarecido e, como mencionado anteriormente, se houver algo que você não tem certeza se precisa ou não, geralmente é mais seguro deixar os cookies ativados, caso interaja com um dos recursos que você usa em nosso site.

Esta política é efetiva a partir de {data_atual}."""
    politica_textbox.delete("1.0", tk.END)  # Limpa o texto anterior
    politica_textbox.insert(tk.END, politica_text)

    # Copia o texto da política para a área de transferência
    pyperclip.copy(politica_text)
    status_label.config(text="Política de Privacidade copiada para a área de transferência!\nAperte CTRL + V para Colar")
    
def gerar_politica_html():
    nome_site = nome_site_entry.get()
    dominio_site = dominio_site_entry.get()
    data_atual = date.today().strftime("%d/%m/%Y")

    politica_text = f"""<h2>Política Privacidade</h2>
<p>A sua privacidade é importante para nós. É política do {nome_site} respeitar a
        sua privacidade em relação a qualquer informação sua que possamos coletar no site <a
            href="{dominio_site}">{nome_site}</a>, e outros sites que possuímos e operamos.</p>
<p>Solicitamos informações pessoais apenas quando realmente precisamos delas para
        lhe fornecer um serviço. Fazemo-lo por meios justos e legais, com o seu conhecimento e consentimento. Também
        informamos por que estamos coletando e como será usado.</p>
<p>Apenas retemos as informações coletadas pelo tempo necessário para fornecer o
        serviço solicitado. Quando armazenamos dados, protegemos dentro de meios comercialmente aceitáveis ​​para evitar
        perdas e roubos, bem como acesso, divulgação, cópia, uso ou modificação não autorizados.</p>
<p>Não compartilhamos informações de identificação pessoal publicamente ou com
        terceiros, exceto quando exigido por lei.</p>
<p>O nosso site pode ter links para sites externos que não são operados por nós.
        Esteja ciente de que não temos controle sobre o conteúdo e práticas desses sites e não podemos aceitar
        responsabilidade por suas respectivas&nbsp;políticas de privacidade.</p>
<p>Você é livre para recusar a nossa solicitação de informações pessoais,
        entendendo que talvez não possamos fornecer alguns dos serviços desejados.</p>
<p>O uso continuado de nosso site será considerado como aceitação de nossas
        práticas em torno de privacidade e informações pessoais. Se você tiver alguma dúvida sobre como lidamos com
        dados do usuário e informações pessoais, entre em contato conosco.</p>
<p>
        <ul>
            <li>O serviço Google AdSense que usamos para veicular publicidade usa
                    um cookie DoubleClick para veicular anúncios mais relevantes em toda a Web e limitar o número de
                    vezes que um determinado anúncio é exibido para você.</li>
            <li>Para mais informações sobre o Google AdSense, consulte as FAQs
                    oficiais sobre privacidade do Google AdSense.</li>
            <li>Utilizamos anúncios para compensar os custos de funcionamento
                    deste site e fornecer financiamento para futuros desenvolvimentos. Os cookies de publicidade
                    comportamental usados ​​por este site foram projetados para garantir que você forneça os anúncios
                    mais relevantes sempre que possível, rastreando anonimamente seus interesses e apresentando coisas
                    semelhantes que possam ser do seu interesse.</li>
            <li>Vários parceiros anunciam em nosso nome e os cookies de
                    rastreamento de afiliados simplesmente nos permitem ver se nossos clientes acessaram o site através
                    de um dos sites de nossos parceiros, para que possamos creditá-los adequadamente e, quando
                    aplicável, permitir que nossos parceiros afiliados ofereçam qualquer promoção que pode fornecê-lo
                    para fazer uma compra.</li>
        </ul>
        <p><br></p>
    </p>
<h3>Compromisso do Usuário</h3>
<p>O usuário se compromete a fazer uso adequado dos conteúdos e da informação que
        o {nome_site} oferece no site e com caráter enunciativo, mas não limitativo:</p>
<ul>
    <li>A) Não se envolver em atividades que sejam ilegais ou contrárias à boa fé
            a à ordem pública;</li>
    <li>B) Não difundir propaganda ou conteúdo de natureza racista, xenofóbica, jogos de azar, qualquer tipo de pornografia ilegal, de
            apologia ao terrorismo ou contra os direitos humanos;</li>
    <li>C) Não causar danos aos sistemas físicos (hardwares) e lógicos (softwares)
            do {nome_site}, de seus fornecedores ou terceiros, para introduzir ou disseminar vírus informáticos ou
            quaisquer outros sistemas de hardware ou software que sejam capazes de causar danos anteriormente
            mencionados.</li>
</ul>
<h3>Mais informações</h3>
<p>Esperemos que esteja esclarecido e, como mencionado anteriormente, se houver
        algo que você não tem certeza se precisa ou não, geralmente é mais seguro deixar os cookies ativados, caso
        interaja com um dos recursos que você usa em nosso site.</p>
<p>Esta política é efetiva a partir de {data_atual}</p>"""

    politica_textbox.delete("1.0", tk.END)  # Limpa o texto anterior
    politica_textbox.insert(tk.END, politica_text)

    # Copia o texto da política para a área de transferência
    pyperclip.copy(politica_text)
    status_label.config(text="Política de Privacidade copiada para a área de transferência!\nAperte CTRL + V para Colar")


# Configuração da janela principal
window = tk.Tk()
window.title("4W Gerador de Política de Privacidade")
window.geometry("500x500")
window.configure(padx=10, pady=10)

# Configurar redimensionamento da grade para centralizar os elementos
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)
window.grid_rowconfigure(5, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# Labels
titulo_label = tk.Label(window, text="4W Sites Gerador de Políticas de Privacidade", font=("Open Sans", 11))
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)


nome_site_label = tk.Label(window, text="Nome do Site:", anchor='w', justify='left')
print(nome_site_label)
nome_site_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')

nome_site_entry = tk.Entry(window, width=40)  # Aumenta o tamanho do campo de entrada
nome_site_entry.grid(row=1, column=1, padx=10, pady=5)

dominio_site_label = tk.Label(window, text="(URL) Domínio do Site:", anchor='w', justify='left')
dominio_site_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')

dominio_site_entry = tk.Entry(window, width=40)  # Aumenta o tamanho do campo de entrada
dominio_site_entry.grid(row=2, column=1, padx=10, pady=5)


# Botão de Gerar Texto
gerar_button = tk.Button(window, text="Gerar Texto ", command=gerar_politica_texto, padx=10, pady=5)
gerar_button.grid(row=3, column=0, pady=10)

# Botão de Gerar HTML
gerar_button_html = tk.Button(window, text="Gerar Texto em HTML", command=gerar_politica_html, padx=10, pady=5)
gerar_button_html.grid(row=3, column=1, pady=10)


# Caixa de texto
politica_textbox = tk.Text(window, height=10, width=40)
politica_textbox.grid(row=4, column=0, columnspan=2, padx=10)

# Label de status
status_label = tk.Label(window, text="")
status_label.grid(row=5, column=0, columnspan=2)

window.mainloop()
