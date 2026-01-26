# View Networks

- Autor: Edilberto Fonseca <edilberto.fonseca@outlook.com>
- Data de criação: 08/07/2022
- **Licença**: [GPL v2](https://www.gnu.org/licenses/gpl-2.0.html)

---

O **View Networks** é um add-on para o NVDA que permite **listar redes Wi-Fi salvas no Windows** e **exibir todos os detalhes de uma rede específica**, incluindo a senha **quando esta estiver armazenada no sistema**.

⚠️ **Importante**  
Este add-on **não quebra, não força e não tenta descobrir senhas de Wi-Fi**.  
Ele apenas exibe informações **já salvas pelo próprio Windows**, da mesma forma que o comando `netsh wlan show profile`.

---

## Novidades da versão atual

- Interface **unificada em uma única janela**
- Dois botões principais:
  - **Listar redes salvas**
  - **Mostrar detalhes da rede**
- Campo único de exibição, mostrando o **conteúdo completo**, exatamente como no Prompt de Comando
- Seleção manual de **codificação (encoding)**:
  - `cp850` (padrão)
  - `cp1252`
  - `latin1`
  - `utf-8`
- Detecção automática de:
  - Ausência de placa Wi-Fi
  - Computadores conectados apenas por cabo
  - Serviço WLAN desativado
- Compatível com sistemas **sem Wi-Fi**, sem causar erros ou reinício do NVDA

---

## Como usar

O add-on pode ser acessado:

- Pelo **menu Ferramentas do NVDA**
- Ou por **atalho de teclado**, Windows + Alt + N - Abre o diálogo principal do View Networks

### Diálogo principal

Ao abrir o View Networks, o usuário encontrará:

1. **Campo de seleção de codificação**  
   Permite escolher a codificação usada pelo Windows para exibição correta dos textos.

2. **Botão “Listar redes salvas”** Alt+ l  
   Exibe todas as redes Wi-Fi armazenadas no sistema.

3. **Botão “Mostrar detalhes da rede”** Alt+ m  
   Solicita o nome da rede e exibe **todas as informações disponíveis**, incluindo a senha, se existente.

4. **Campo de texto principal**  
   Mostra o resultado completo do comando `netsh`, sem filtros ou alterações.

5. **Botão Fechar** Alt+ f  
   Encerra o diálogo.

---

## Comportamento em PCs sem Wi-Fi

Caso o computador:

- não possua placa Wi-Fi, ou
- esteja usando apenas conexão via cabo,

o add-on exibirá uma mensagem clara informando que **nenhuma interface Wi-Fi foi detectada**, junto com o diagnóstico retornado pelo sistema.
