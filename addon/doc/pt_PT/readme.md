# View Networks

- Autor: Edilberto Fonseca <edilberto.fonseca@outlook.com>
- Data de criação: 08/07/2022
- **Licença**: [GPL v2](https://www.gnu.org/licenses/gpl-2.0.html)

---

O **View Networks** é um extra para o NVDA que permite **listar redes Wi-Fi guardadas no Windows** e **mostrar todos os detalhes de uma rede específica**, incluindo a palavra-passe **quando esta se encontra armazenada no sistema**.

⚠️ **Importante**
Este extra **não quebra, não força nem tenta descobrir palavras-passe de Wi-Fi**.
Apenas apresenta informações **já guardadas pelo próprio Windows**, da mesma forma que o comando `netsh wlan show profile`.

---

## Novidades da versão actual

- Interface **unificada numa única janela**
- Dois botões principais:
  - **Listar redes guardadas**
  - **Mostrar detalhes da rede**
- Campo único de visualização, apresentando o **conteúdo completo**, exactamente como na Linha de Comandos
- Selecção manual de **codificação (encoding)**:
  - `cp850` (padrão)
  - `cp1252`
  - `latin1`
  - `utf-8`
- Detecção automática de:
  - Ausência de placa Wi-Fi
  - Computadores ligados apenas por cabo
  - Serviço WLAN desactivado
- Compatível com sistemas **sem Wi-Fi**, sem provocar erros ou reinício do NVDA

---

## Como utilizar

O extra pode ser acedido:

- Através do **menu Ferramentas do NVDA**
- Ou através de **atalho de teclado**, Windows + Alt + N — Abre o diálogo principal do View Networks

### Diálogo principal

Ao abrir o View Networks, o utilizador encontrará:

1. **Campo de selecção de codificação**
   Permite escolher a codificação utilizada pelo Windows para a correcta apresentação dos textos.

2. **Botão “Listar redes guardadas”** Alt + L
   Mostra todas as redes Wi-Fi guardadas no sistema.

3. **Botão “Mostrar detalhes da rede”** Alt + M
   Solicita o nome da rede e apresenta **todas as informações disponíveis**, incluindo a palavra-passe, se existir.

4. **Campo de texto principal**
   Mostra o resultado completo do comando `netsh`, sem filtros ou alterações.

5. **Botão Fechar** Alt + F
   Fecha o diálogo.

---

## Comportamento em computadores sem Wi-Fi

Caso o computador:

- não possua placa Wi-Fi, ou
- esteja ligado apenas por cabo,

o extra apresentará uma mensagem clara a informar que **nenhuma interface Wi-Fi foi detectada**, juntamente com o diagnóstico devolvido pelo sistema.
