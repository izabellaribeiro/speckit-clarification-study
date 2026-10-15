# Temas das histórias do experimento

Esta descrição deriva dos textos preparados no manifesto e dos 15 baselines
recuperados no arquivo `experimento-icse.zip`. Os rótulos dos datasets seguem o
manifesto existente; o tema de uma história não comprova sua origem externa.

| Dataset no manifesto | Histórias-pai | Temas presentes nos textos |
| --- | --- | --- |
| Zooniverse | 25: US_001–US_015 e US_036–US_045 | Recomendação musical e de conteúdo; descoberta audiovisual por localização; qualidade, edição e direitos de conteúdo; detecção de pessoas, produtos e logos; segmentação de vídeos; engajamento, confiabilidade e assistência a voluntários; revisão de anotações e processamento de imagens de fauna. |
| PlanningPoker | 10: US_016–US_025 | Criação de sessões de estimativa ágil, convite de estimadores, rodadas, gestão de itens, registro de estimativas, importação de histórias e exportação de resultados. |
| BADCamp | 10: US_026–US_035 | Participação em conferências, patrocinadores e perfis, mapas e locais, inscrições e listas de espera em treinamentos, inscrições em encontros, programação e comunicação do evento. |

Cada história-pai participa das quatro condições. Esses números descrevem as
45 histórias-pai, não a distribuição das 100 perguntas selecionadas.

A pesquisadora informou que a seleção de 25 perguntas por condição considerou
temas e datasets diferentes. Não foram informadas cotas por tema/dataset nem
uma regra reproduzível por item. Os agrupamentos descritivos acima foram
documentados a partir dos textos disponíveis e não devem ser apresentados como
categorias ou cotas predefinidas na seleção original.

## Histórico recuperado para as 15 histórias anteriores

Os arquivos `inputs/1_baseline/US_001.md` a `US_015.md` do experimento anterior
foram preservados em `legacy_baselines/`. Todos correspondem ao texto das entradas
baseline atuais após desconsiderar BOM UTF-8 e espaços externos. Os snapshots Git
do ZIP também contêm os 15 textos; `legacy_history.csv` registra os commits e blobs
correspondentes, sem importar contas, emails ou o diretório `.git` original.
`legacy_archive_record.json` registra o hash SHA-256 do ZIP recebido.

Essa recuperação estabelece a origem imediata no experimento anterior. O ZIP não
contém os arquivos-fonte públicos com mapeamentos por linha para essas 15 histórias
nem documenta sua seleção inicial ou a remoção prévia de cláusulas de benefício.
Portanto, essa parte da proveniência original continua em aberto. Para as 30 adições,
os mapeamentos de arquivo, linha e texto-fonte já existentes foram mantidos.


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
