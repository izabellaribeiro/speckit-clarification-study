#!/usr/bin/env python3
import csv,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent
PAT=re.compile(r'\[NEEDS CLARIFICATION:\s*([^\]\n]+)\]')
rows=[]
for d in sorted((ROOT/'results_new').glob('US_*_*')) if (ROOT/'results_new').exists() else []:
 meta_file=d/'metadata.json';response_file=d/'final_response.md'
 if not meta_file.exists() or not response_file.exists():continue
 meta=json.loads(meta_file.read_text(encoding='utf8'))
 response=response_file.read_text(encoding='utf8')
 for i,m in enumerate(PAT.finditer(response),1):
  prefix=response[max(0,m.start()-700):m.start()].strip()
  # preserve context; do not pretend it is a cleanly parsed question
  rows.append({'story_id':meta['story_id'],'condition':meta['condition'],'marker_number':i,'risk':m.group(1).strip(),
   'preceding_text_raw':prefix,'response_path':str(response_file.relative_to(ROOT)),
   'substantive_review':'','targeted_injected_defect':'','macro_category':'','expert_notes':''})
fields=['story_id','condition','marker_number','risk','preceding_text_raw','response_path','substantive_review','targeted_injected_defect','macro_category','expert_notes']
with (ROOT/'markers_for_review.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
print('Extracted raw markers:',len(rows),'(NOT validated substantive clarifications)')
