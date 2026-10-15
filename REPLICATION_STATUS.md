# Registro dos materiais de replicação

## Publicação

O repositório público ainda não foi criado e não existe URL pública verificada.
Não inserir um endereço fictício em `Replication Materials`.
`prepare_release.py` prepara `release_candidate/` sem modificar os registros originais.
A cópia inclui as 180 execuções (logs, respostas e metadados), entradas, runner,
extrator, constituição, skill, planilhas, classificação final em CSV e proveniência.
O manifesto registra hashes da cópia anonimizada. Os hashes experimentais existentes
continuam identificando os arquivos originais, que podem diferir das cópias sanitizadas.

A anonimização automática remove caminhos absolutos locais, emails e o nome/conta
conhecidos da pesquisadora. Antes da publicação, revisar manualmente os arquivos,
inclusive nomes, links e identificadores contextuais que não sejam capturados por
esses padrões. Manter `results_new/`, backups e planilhas originais em armazenamento
privado; publicar apenas a cópia revisada. Não publicar esta árvore inteira sem revisão.
Depois de publicar, verificar o acesso sem autenticação e atualizar o artigo com a URL.

## Consenso humano

A pesquisadora informou revalidação por dois especialistas humanos, sem participação
de IA nas decisões de classificação. Não foi fornecida uma data de revisão.
`reference/final_audit.xlsx` permanece intacta. A cópia
`reference/final_audit_documented.xlsx` acrescenta `Review Record` e conserva todas
as abas e valores anteriores, inclusive as notas provisórias, como histórico.
O registro atual aponta para os rótulos da aba `Final`; não houve nova classificação
por IA nesta atualização. A confirmação não estabelece a independência das duas
colunas anteriores: não apresentar kappa como confiabilidade humana.
A abrangência da revalidação sobre os 135 mutantes ainda precisa ser esclarecida;
não confundir consenso sobre perguntas com validação de defeitos nas histórias.

## Seleção das perguntas

As 100 perguntas incluem 25 de cada condição. Segundo a pesquisadora, a seleção
considerou diferentes temas e datasets. Trata-se de seleção intencional, não aleatória.
Não foram fornecidos critérios reproduzíveis por item, cotas por tema/dataset ou
uma ordenação de seleção. Não inferir esses detalhes nem estimar prevalência nas
894 perguntas a partir desta amostra. A revalidação humana não muda essa limitação.

## Proveniência

`reference/story_provenance.csv` deriva do manifesto existente e reúne os 45 pais.
As 30 adições têm arquivo-fonte, linha, texto-fonte e baseline preparado registrados.
Preservar esses mapeamentos e a remoção das cláusulas de benefício, com possível
normalização do ator, conforme descrito no artigo. Essa preparação pode gerar
pedidos de esclarecimento. Para os 15 casos antigos, o manifesto registra apenas
baselines arquivados; fontes detalhadas e histórico anterior não estão disponíveis
nos registros examinados. Não reconstruir ou inventar essa origem.


## Temas dos datasets

Os temas descritivos das hist?rias est?o em `reference/dataset_themes.md` e na
coluna `theme_summary` de `story_provenance.csv`. N?o representam cotas
reconstru?das da sele??o das 100 perguntas. Os r?tulos de projeto do manifesto
foram preservados; sem fontes originais para os casos antigos, n?o os
reclassificamos a partir do tema.


## Compara??o com os datasets fornecidos posteriormente

As tr?s c?pias recebidas est?o em `reference/source_datasets/`, com hashes em
`source_manifest.json`. A verifica??o confirmou texto e linha das 30 adi??es.
Para US_001, a linha 4 de `g28-zooniverse-uploaded.txt` coincide com o baseline
ap?s retirar a cl?usula de benef?cio. Para as outras 14 hist?rias antigas,
`reference/legacy_source_comparison.csv` registra correspond?ncias candidatas e
diferen?as de reda??o. Esses v?nculos ainda precisam de confirma??o hist?rica
pela pesquisadora; sem isso, n?o equivalem a mapeamentos de origem comprovados.
O ZIP n?o continha as fontes externas, mas agora elas foram fornecidas separadamente.
A sequ?ncia de edi??o anterior ao experimento permanece sem documenta??o.


## Confirma??o posterior da pesquisadora

A pesquisadora confirmou que as 14 hist?rias antigas com diferen?as de reda??o
foram adaptadas das correspond?ncias identificadas nos datasets fornecidos.
Os campos `source_file`, `source_line` e `source_full_text` agora registram esses
v?nculos; `source_verification` distingue a confirma??o humana da coincid?ncia
textual. Os campos `candidate_source_*` preservam o registro da investiga??o
anterior, n?o uma pend?ncia atual. As diferen?as de reda??o permanecem preservadas.
N?o foi informada data da adapta??o nem sua sequ?ncia detalhada de edi??o.
Esta confirma??o atualiza as ressalvas anteriores sobre os v?nculos candidatos.
O artigo n?o foi atualizado nesta etapa, por solicita??o da pesquisadora.
