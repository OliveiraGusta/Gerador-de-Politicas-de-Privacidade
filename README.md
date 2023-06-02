# Gerador de Políticas de Privacidade

Este é um projeto em Python que implementa um gerador de políticas de privacidade simples. Ele permite gerar uma política de privacidade personalizada com base no nome e domínio do site fornecidos.


## Funcionalidades
- Interface gráfica amigável usando Tkinter.
- Campos para inserir o nome do site e o domínio do site.
- Geração automática da política de privacidade com base nos dados fornecidos.
- Exibição da política de privacidade gerada em uma caixa de texto.
- Cópia automática da política de privacidade para a área de transferência.
- Exibição de uma mensagem de status informando que a política de privacidade foi copiada com sucesso.


## Pré-requisitos
- Python 3.x
- Bibliotecas: tkinter, datetime, pyperclip


## Instalação e Uso
1. Faça o download dos arquivos do projeto.
2. Certifique-se de ter as bibliotecas necessárias instaladas. Caso contrário, instale-as usando o comando pip install tkinter datetime pyperclip.
3. Navegue até o diretório onde estão localizados os arquivos do projeto.
4. Execute o comando python gerador_politicas.py para iniciar o aplicativo.
5. Na janela exibida, preencha o nome do site e o domínio do site nos campos correspondentes.
6. Clique no botão "Gerar" para gerar a política de privacidade.
7. A política de privacidade gerada será exibida na caixa de texto.
8. A política de privacidade também será copiada automaticamente para a área de transferência.
9. Verifique a mensagem de status exibida na parte inferior da janela, confirmando que a política de privacidade foi copiada com sucesso.

## Construção do Executável

Você também pode criar um arquivo executável (.exe) a partir do script Python usando o PyInstaller. Certifique-se de ter o PyInstaller instalado e siga estas etapas:

1. Abra o terminal ou prompt de comando.
2. Navegue até o diretório onde está localizado o arquivo gerador_politicas.py.
3. Execute o comando pyinstaller --onefile gerador_politicas.py.
4. Aguarde até que o PyInstaller crie o arquivo executável.
5. Após a conclusão do processo, o arquivo executável será criado no diretório dist com o nome gerador_politicas.exe.

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou correções, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é licenciado sob a MIT License.

___
Esse é um projeto simples para gerar políticas de privacidade personalizadas. Sinta-se à vontade para utilizá-lo, adaptá-lo ou melhorá-lo de acordo com suas necessidades.
