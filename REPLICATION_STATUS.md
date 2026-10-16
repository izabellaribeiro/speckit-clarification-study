# Registro dos materiais de replicação

## Publicação

Os materiais de replica??o s?o disponibilizados para avalia??o pelo endere?o an?nimo:
https://anonymous.4open.science/r/speckit-clarification-study-111B/

Esta ? a c?pia de refer?ncia para compara??o com o artigo. A afirma??o hist?rica
de que o reposit?rio ainda n?o havia sido criado est? superada. O acesso pelo
servi?o an?nimo n?o foi verificado nesta atualiza??o.

A se??o Replication Materials do manuscrito deve usar o endere?o an?nimo e
identificar a vers?o analisada sem expor a conta ou o reposit?rio de origem.

`prepare_release.py` é o script de preparação original. Os arquivos de documentação
da cópia publicada foram atualizados posteriormente; uma nova preparação deve
preservar essas atualizações. O manifesto registra os hashes atuais da cópia
sanitizada e exclui a si próprio. Os hashes experimentais continuam identificando
os arquivos originais, que podem diferir das cópias sanitizadas. A anonimização
automática original não certifica a remoção de todos os identificadores contextuais.
Manter backups e registros privados separados dos materiais publicados.

## Correspondência com o artigo revisado

A recontagem dos marcadores nas 180 respostas de `results_new/` confirma 894 itens:
224 baseline, 221 sintáticos, 224 semânticos e 225 pragmáticos. Há 176 execuções
com cinco itens e 131 comparações baseline–variante com contagens iguais.
A classificação final contém 100 perguntas, com 76 rótulos Classical Normative
Scope e 24 Extended Scope (New AI Dimension), denominados no artigo requirements
concerns e operational detail, respectivamente. Esses números descrevem contagens
e conteúdo; não são taxas de detecção dos defeitos pretendidos.

## Consenso humano

A pesquisadora informou revalidação por dois especialistas humanos, sem participação
de IA nas decisões de classificação. Não foi fornecida uma data de revisão.
`reference/final_audit_documented.xlsx` acrescenta Review Record e conserva as abas
e valores anteriores, inclusive notas provisórias, como histórico. O registro atual
aponta para os rótulos da aba Final, exportados em `final_classification.csv`;
não houve nova classificação por IA nesta atualização.

A confirmação não estabelece a independência das duas colunas anteriores:
não apresentar kappa como confiabilidade humana. Consenso sobre perguntas não
estabelece validação independente dos defeitos nas 135 variantes. O artigo não
reivindica essa validação nem cobertura de detecção para o conjunto completo.

## Seleção das perguntas

As 100 perguntas incluem 25 de cada condição, provenientes de 77 execuções e
39 histórias-pai. Segundo a pesquisadora, a seleção considerou diferentes temas
e datasets. Trata-se de seleção intencional, não aleatória. Não foram fornecidos
critérios reproduzíveis por item, cotas por tema/dataset ou ordenação de seleção.
Não inferir esses detalhes nem estimar prevalência nas 894 perguntas a partir
desta amostra. A revalidação humana não muda essa limitação.

## Proveniência e confirmação posterior

`reference/story_provenance.csv` reúne os 45 pais e distingue texto-fonte,
baseline preparado e variante. As 30 adições têm arquivo-fonte, linha e texto-fonte
registrados; a comparação com os datasets fornecidos confirmou esses vínculos.
A preparação removeu cláusulas de benefício e pode ter normalizado atores,
criando necessidades de esclarecimento já nos baselines.

Para US_001, a linha 4 de `g28-zooniverse-uploaded.txt` coincide com o baseline
após retirar a cláusula de benefício. Para as outras 14 histórias antigas,
`reference/legacy_source_comparison.csv` preserva correspondências e diferenças
de redação. A pesquisadora posteriormente confirmou que essas histórias foram
adaptadas das correspondências identificadas nos datasets. Os campos `source_file`,
`source_line` e `source_full_text` registram esses vínculos; `source_verification`
distingue confirmação humana de coincidência textual. Os campos `candidate_source_*`
preservam a investigação anterior, não uma pendência atual.

Essa confirmação supera as ressalvas históricas sobre vínculos candidatos.
Não foram informadas a data nem a sequência detalhada das adaptações; não
reconstruir essa história. As fontes fornecidas posteriormente estão em
`reference/source_datasets/`, com hashes em `source_manifest.json`.

## Temas dos datasets

Os temas descritivos estão em `reference/dataset_themes.md` e em `theme_summary`
de `story_provenance.csv`. Não representam cotas reconstruídas da seleção das
100 perguntas. Os rótulos de projeto do manifesto foram preservados.
