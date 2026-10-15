#!/usr/bin/env python3
"""SAC 2027 protocol adaptation. Python standard library only. Expert review remains a separate analysis stage."""
import argparse,hashlib,json,random,shutil,subprocess,sys,time,re
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parent
CONDITIONS=('baseline','syntactic','semantic','pragmatic')
MARKER=re.compile(r'\[NEEDS CLARIFICATION:\s*([^\]\n]+)\]')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 p=argparse.ArgumentParser()
 p.add_argument('--model',default='gpt-6.1-sol')
 p.add_argument('--story',default='US_001')
 p.add_argument('--condition',choices=CONDITIONS,default='baseline')
 p.add_argument('--pilot',action='store_true',help='one story, one condition')
 p.add_argument('--all',action='store_true',help='all 180 cases')
 p.add_argument('--dry-run',action='store_true')
 p.add_argument('--seed',type=int,default=2027)
 p.add_argument('--max-runs',type=int)
 a=p.parse_args()
 if a.pilot==a.all:p.error('choose exactly one of --pilot or --all')
 cases=[(f'US_{i:03d}',c) for i in range(1,46) for c in CONDITIONS] if a.all else [(a.story,a.condition)]
 if a.all:
  random.Random(a.seed).shuffle(cases)
 if a.max_runs is not None:cases=cases[:a.max_runs]
 template=ROOT/'speckit_codex'
 assert (template/'.agents/skills/speckit-clarify/SKILL.md').exists()
 assert '[NEEDS CLARIFICATION:' in (template/'.specify/memory/constitution.md').read_text(encoding='utf8')
 for sid,cond in cases:
  if not (ROOT/'inputs'/cond/f'{sid}.md').is_file():p.error(f'Missing {sid}/{cond}')
 print('Cases:',len(cases),'Model:',a.model,'Dry-run:',a.dry_run)
 if a.dry_run:return
 codex=shutil.which('codex.cmd') or shutil.which('codex.exe') or shutil.which('codex')
 if not codex:p.error('Codex CLI not found in PATH')
 results=ROOT/'results_new';results.mkdir(exist_ok=True)
 for sid,cond in cases:
  dest=results/f'{sid}_{cond}'
  if (dest/'completed.json').exists():print('SKIP',sid,cond);continue
  if dest.exists():p.error(f'{dest} already exists without completion marker: inspect or move it before rerun')
  dest.mkdir(parents=True)
  work=dest/'workspace'
  shutil.copytree(template,work,ignore=shutil.ignore_patterns('.git','node_modules','.venv','results_new'))
  specdir=work/'specs'/f'001-{sid.lower()}-{cond}';specdir.mkdir(parents=True,exist_ok=True)
  source=ROOT/'inputs'/cond/f'{sid}.md'
  spec=specdir/'spec.md'
  spec.write_text('# User Story under Study\n\n## Original User Story\n\n'+source.read_text(encoding='utf8').strip()+'\n',encoding='utf8')
  (work/'.specify/feature.json').write_text(json.dumps({'feature_directory':str(specdir.resolve())},indent=2),encoding='utf8')
  for other in (work/'specs').iterdir():
   if other.is_dir() and other!=specdir:shutil.rmtree(other)
  prompt=('Use the installed speckit-clarify skill for the active spec. First read AGENTS.md, '
   '.specify/memory/constitution.md, and .agents/skills/speckit-clarify/SKILL.md. '
   'Apply the original constitution and the SpecKit clarification taxonomy. '
   'The current story is the sole requirements input. Do not assume missing facts. '
   'This is a NONINTERACTIVE RESEARCH ADAPTATION: do not ask for human replies, '
   'do not modify files, do not recommend answers, do not implement. '
   'In one final response, list up to five substantive questions, one per numbered item; '
   'immediately follow EACH question with the constitution-required tag '
   '[NEEDS CLARIFICATION: specific reason explaining the precise technical or business risk identified]. '
   'If no substantive questions are justified, explicitly say so. '
   'If prerequisites fail, report the failure instead of inventing a feature.')
  cmd=[codex,'exec','--json','--model',a.model,'--sandbox','read-only','--skip-git-repo-check','-']
  start=datetime.now(timezone.utc).isoformat();t=time.monotonic();before=digest(spec)
  with (dest/'events.jsonl').open('w',encoding='utf8') as stdout,(dest/'stderr.txt').open('w',encoding='utf8') as stderr:
   proc=subprocess.run(cmd,cwd=work,input=prompt,text=True,stdout=stdout,stderr=stderr)
  messages=[];completed=False
  for line in (dest/'events.jsonl').read_text(encoding='utf8').splitlines():
   try:e=json.loads(line)
   except json.JSONDecodeError:continue
   if e.get('type')=='turn.completed':completed=True
   item=e.get('item',{})
   if e.get('type')=='item.completed' and item.get('type')=='agent_message':messages.append(item.get('text',''))
  response='\n\n'.join(messages)
  (dest/'final_response.md').write_text(response,encoding='utf8')
  markers=MARKER.findall(response)
  meta={'story_id':sid,'condition':cond,'model':a.model,'started_utc':start,
   'elapsed_seconds':round(time.monotonic()-t,2),'exit_code':proc.returncode,
   'turn_completed':completed,'input_sha256':digest(source),
   'constitution_sha256':digest(work/'.specify/memory/constitution.md'),
   'skill_sha256':digest(work/'.agents/skills/speckit-clarify/SKILL.md'),
   'spec_unchanged':before==digest(spec),'marker_count_raw':len(markers),
   'warning':'Markers are NOT automatically substantive; manual review required.'}
  (dest/'metadata.json').write_text(json.dumps(meta,indent=2,ensure_ascii=False),encoding='utf8')
  ok=proc.returncode==0 and completed and bool(response.strip()) and meta['spec_unchanged']
  if ok:(dest/'completed.json').write_text(json.dumps({'technical_success':True,'scientific_review':'PENDING'},indent=2),encoding='utf8')
  print(sid,cond,'exit',proc.returncode,'turn',completed,'markers',len(markers),'technical_ok',ok,flush=True)
if __name__=='__main__':main()
