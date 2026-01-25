# View Networks

- **Autor:** Edilberto Fonseca <edilberto.fonseca@outlook.com>
- **Data de criação:** 08/07/2022
- **Última actualização:** 2026

---

O add-on **View Networks** permite listar as redes Wi-Fi guardadas no sistema e visualizar os detalhes completos de uma rede específica, utilizando informações fornecidas pelo próprio Windows através do comando `netsh`.

> ⚠️ **Nota importante:**  
> Este add-on **não quebra, não descodifica nem tenta descobrir palavras-passe de redes Wi-Fi**.  
> O seu funcionamento baseia-se exclusivamente na apresentação de informações **já armazenadas no sistema**, incluindo a palavra-passe **apenas quando o Windows o permite** (redes às quais o utilizador já se ligou anteriormente).

---

## Como utilizar

A utilização do add-on é simples e totalmente acessível com o NVDA.

O View Networks pode ser aberto:

- através do **menu Ferramentas do NVDA**, ou
- por meio de um **atalho de teclado configurado**.

Ao ser aberto, o add-on apresenta **uma única janela**, onde todas as funcionalidades estão centralizadas.

---

## Janela principal (interface unificada)

A janela principal do View Networks reúne todas as funcionalidades num único diálogo, tornando a utilização mais organizada e intuitiva.

### Componentes da janela

1. **Campo “Nome da rede”**
   - Campo opcional
   - Deve ser preenchido apenas quando o utilizador pretender visualizar os detalhes de uma rede específica.

2. **Campo “Encoding” (codificação do texto)**
   - Permite seleccionar a codificação utilizada para interpretar a saída do comando `netsh`.
   - O encoding escolhido é aplicado **tanto à listagem de redes como à visualização de detalhes**.
   - Estão disponíveis as seguintes opções:
     - `cp850` (predefinição)
     - `cp1252`
     - `latin-1`
     - `utf-8`
     - `cp437`

   Esta opção é especialmente útil em sistemas com diferentes idiomas ou configurações regionais do Windows.

3. **Botão “Listar redes guardadas”**
   - Executa o comando:

     ```dos
     netsh wlan show profile
     ```

   - Lista todas as redes Wi-Fi guardadas no sistema.
   - O resultado completo é apresentado no campo de saída.

4. **Botão “Mostrar detalhes da rede”**
   - Utiliza o nome introduzido no campo “Nome da rede”.
   - Executa o comando:

     ```dos
     netsh wlan show profile name="NOME_DA_REDE" key=clear
     ```

   - Apresenta **todo o conteúdo devolvido pelo Windows**, exactamente como surge na Linha de Comandos.
   - Caso o campo esteja vazio, o NVDA informa o utilizador de que é necessário indicar o nome da rede.

5. **Campo de saída (texto multilinha)**
   - Área única onde:
     - é apresentada a lista de redes guardadas, ou
     - são exibidos os detalhes completos de uma rede específica.
   - O foco é automaticamente colocado neste campo após cada operação, facilitando a leitura com o NVDA.

6. **Botão “Copiar”**
   - Copia todo o conteúdo do campo de saída para a área de transferência.
   - Útil para colar em mensagens de correio electrónico, documentos ou pedidos de suporte técnico.

7. **Botão “Fechar”**
   - Fecha a janela do add-on.
   - Pode igualmente ser accionado através da tecla **Escape**.

---

## Acessibilidade

O add-on foi desenvolvido com forte enfoque na acessibilidade:

- Todas as acções produzem **mensagens faladas pelo NVDA**.
- O foco é gerido automaticamente após cada operação.
- Não existem múltiplas janelas ou diálogos confusos.
- Toda a interface pode ser utilizada exclusivamente com o teclado.

---

## Atalhos

Os atalhos de teclado podem variar consoante a configuração do utilizador, mas geralmente incluem:

1. **Windows + Alt + N** – Abre a janela principal do View Networks
2. **Windows + Alt + O** – Apresenta informações sobre o add-on
3. **Windows + Alt + J** – Abre a página de ajuda do add-on

> Nota: Os atalhos podem ser personalizados nas definições de gestos de entrada do NVDA.

---

## Sobre

A opção **Sobre** apresenta informações detalhadas acerca do add-on, incluindo:

- Versão do add-on
- Autor
- Descrição
- Versão mínima do NVDA necessária
- Última versão do NVDA testada

---

## Considerações finais

A versão actual do View Networks oferece:

- Interface unificada e mais organizada
- Maior estabilidade
- Melhor compatibilidade com diferentes idiomas do Windows
- Experiência significativamente melhorada para utilizadores de leitores de ecrã

O add-on evoluiu no sentido de proporcionar **clareza, controlo e acessibilidade**, respeitando sempre as limitações e a segurança definidas pelo próprio sistema operativo.
