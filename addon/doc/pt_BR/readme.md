# View Networks

- **Autor:** Edilberto Fonseca <edilberto.fonseca@outlook.com>
- **Data de criação:** 08/07/2022
- **Última atualização:** 2026

---

O add-on **View Networks** permite listar as redes Wi-Fi salvas no sistema e exibir os detalhes completos de uma rede específica, utilizando informações fornecidas pelo próprio Windows através do comando `netsh`.

> ⚠️ **Observação importante:**  
> Este add-on **não quebra, descriptografa ou tenta adivinhar senhas de Wi-Fi**.  
> Ele apenas exibe informações **já armazenadas no sistema**, incluindo a senha **somente quando o Windows permite** (ou seja, redes previamente conectadas no dispositivo).

---

## Como usar

O uso do add-on é simples e totalmente acessível com o NVDA.

Ele pode ser aberto:

- pelo **menu Ferramentas do NVDA**, ou
- pelo **atalho de teclado configurado**.

Ao ser aberto, o add-on apresenta **uma única janela**, onde todas as funcionalidades estão concentradas.

---

## Janela principal (interface unificada)

A janela principal do View Networks reúne todas as funções em um único diálogo, tornando o uso mais organizado e intuitivo.

### Componentes da janela

1. **Campo “Nome da rede”**
   - Opcional
   - Deve ser preenchido apenas quando o usuário quiser exibir os detalhes de uma rede específica.

2. **Campo “Encoding” (codificação do texto)**
   - Permite escolher a codificação usada para interpretar a saída do comando `netsh`.
   - O encoding selecionado é utilizado **tanto para listar redes quanto para mostrar detalhes**.
   - Opções disponíveis incluem:
     - `cp850` (padrão)
     - `cp1252`
     - `latin-1`
     - `utf-8`
     - `cp437`

   Esse recurso é especialmente útil em sistemas com idioma ou configuração regional diferentes.

3. **Botão “Listar redes salvas”**
   - Executa o comando:

     ```dos
     netsh wlan show profile
     ```

   - Lista todas as redes Wi-Fi salvas no sistema.
   - O resultado completo é exibido no campo de saída.

4. **Botão “Mostrar detalhes da rede”**
   - Utiliza o nome informado no campo “Nome da rede”.
   - Executa o comando:

     ```dos
     netsh wlan show profile name="NOME_DA_REDE" key=clear
     ```

   - Exibe **todo o conteúdo retornado pelo Windows**, exatamente como aparece no Prompt de Comando.
   - Caso o campo esteja vazio, o NVDA informa que é necessário digitar o nome da rede.

5. **Campo de saída (texto multilinha)**
   - Área única onde:
     - a lista de redes é exibida, ou
     - os detalhes completos de uma rede específica são mostrados.
   - O foco é movido automaticamente para esse campo após cada ação, facilitando a leitura com o NVDA.

6. **Botão “Copiar”**
   - Copia todo o conteúdo exibido no campo de saída para a área de transferência.
   - Útil para colar em e-mails, documentos ou enviar para suporte técnico.

7. **Botão “Fechar”**
   - Fecha a janela do add-on.
   - Também pode ser acionado pela tecla **Escape**.

---

## Acessibilidade

O add-on foi projetado com foco total em acessibilidade:

- Todas as ações geram **mensagens faladas pelo NVDA**.
- O foco é controlado automaticamente após cada operação.
- Não há abertura de múltiplas janelas ou diálogos confusos.
- A interface é totalmente navegável pelo teclado.

---

## Atalhos

Os atalhos podem variar conforme a configuração do usuário, mas normalmente incluem:

1. **Windows + Alt + N** – Abre a janela principal do View Networks
2. **Windows + Alt + O** – Exibe informações sobre o add-on
3. **Windows + Alt + J** – Abre a página de ajuda do add-on

> Obs.: Os atalhos podem ser personalizados nas configurações de gestos de entrada do NVDA.

---

## Sobre

A opção **Sobre** exibe informações detalhadas do add-on, incluindo:

- Versão do add-on
- Autor
- Descrição
- Versão mínima do NVDA necessária
- Última versão do NVDA testada

---

## Considerações finais

A versão atual do View Networks apresenta:

- Interface unificada e mais organizada
- Maior estabilidade
- Melhor compatibilidade com diferentes idiomas do Windows
- Melhor experiência para usuários de leitores de tela

O add-on evoluiu para oferecer **clareza, controle e acessibilidade**, mantendo sempre o compromisso com a segurança e os limites impostos pelo próprio sistema operacional.
