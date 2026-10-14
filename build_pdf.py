"""Build the PDF from the repository's authoritative Markdown lesson files.

Requires reportlab. Optional environment variable TUTORIAL_FONT_DIR can point to
a directory containing DejaVuSans.ttf, DejaVuSans-Bold.ttf and DejaVuSansMono.ttf.
If those fonts are unavailable, the standard PDF fonts are used.
"""
import csv
import html
import json
import os
import re
from pathlib import Path
from urllib.parse import quote

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether, Preformatted, Flowable
from reportlab.platypus.tableofcontents import TableOfContents

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / 'tutorial.json').read_text())
OUTPUT = ROOT / 'Working_With_AI_Agents_Tutorial.pdf'
FONT_DIR = Path(os.environ.get('TUTORIAL_FONT_DIR', '/usr/share/fonts/truetype/dejavu'))
if all((FONT_DIR / f).exists() for f in ('DejaVuSans.ttf','DejaVuSans-Bold.ttf','DejaVuSansMono.ttf')):
    for name,file in [('Guide','DejaVuSans.ttf'),('GuideBold','DejaVuSans-Bold.ttf'),('GuideMono','DejaVuSansMono.ttf')]:
        pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / file)))
    pdfmetrics.registerFontFamily('Guide', normal='Guide', bold='GuideBold', italic='Guide', boldItalic='GuideBold')
    F,B,M = 'Guide','GuideBold','GuideMono'
else:
    F,B,M = 'Helvetica','Helvetica-Bold','Courier'

NAVY = colors.HexColor('#112940')
TEAL = colors.HexColor('#087F82')
INK = colors.HexColor('#223447')
MUTED = colors.HexColor('#566779')
PALE = colors.HexColor('#EDF5F7')
PAGE_W,PAGE_H = A4
WIDTH = PAGE_W - 104
STYLE = {
 'body': ParagraphStyle('Body',fontName=F,fontSize=10.1,leading=15.1,textColor=INK,spaceAfter=8),
 'small': ParagraphStyle('Small',fontName=F,fontSize=8.6,leading=12.4,textColor=MUTED,spaceAfter=6),
 'h1': ParagraphStyle('Chapter',fontName=B,fontSize=26,leading=32,textColor=NAVY,spaceBefore=8,spaceAfter=16,keepWithNext=True),
 'h2': ParagraphStyle('Lesson',fontName=B,fontSize=15,leading=20,textColor=NAVY,spaceBefore=16,spaceAfter=10,keepWithNext=True),
 'h3': ParagraphStyle('Section',fontName=B,fontSize=9.4,leading=13.5,textColor=TEAL,spaceBefore=9,spaceAfter=5,keepWithNext=True),
 'label': ParagraphStyle('Label',fontName=B,fontSize=9,leading=12,textColor=TEAL,spaceAfter=9,keepWithNext=True),
 'title': ParagraphStyle('CoverTitle',fontName=B,fontSize=42,leading=48,textColor=NAVY,spaceAfter=22),
 'subtitle': ParagraphStyle('Subtitle',fontName=F,fontSize=15,leading=22,textColor=MUTED,spaceAfter=16),
 'bullet': ParagraphStyle('Bullet',fontName=F,fontSize=10.1,leading=15.1,textColor=INK,leftIndent=15,firstLineIndent=-15,spaceAfter=5),
 'source': ParagraphStyle('Source',fontName=F,fontSize=8.2,leading=11.8,textColor=MUTED,spaceAfter=4,wordWrap='CJK'),
 'code': ParagraphStyle('Code',fontName=M,fontSize=7.7,leading=11,textColor=INK,spaceAfter=10),
}


def inline(text, relative_to=None):
    text = html.escape(text)
    text = text.replace('&lt;br/&gt;', '<br/>')
    def link(match):
        label,url = match.group(1),html.unescape(match.group(2))
        if not url.startswith(('https://','http://')):
            base = ROOT if relative_to is None else relative_to
            target = (base / url.split('#')[0]).resolve()
            try: rel = target.relative_to(ROOT).as_posix()
            except ValueError: rel = 'README.md'
            url = 'https://github.com/Adedaved/Working-With-AI-Agents/blob/tutorial/ibm-ai-agents/' + quote(rel)
        return f'<a href="{html.escape(url, quote=True)}" color="#087F82">{label}</a>'
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,text)
    text = re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',text)
    text = re.sub(r'`([^`]+)`',lambda m:f'<font name="{M}" size="9">{m.group(1)}</font>',text)
    return text


def P(text,style='body',relative_to=None):
    return Paragraph(inline(text,relative_to), STYLE[style])


class CoverBand(Flowable):
    def __init__(self):
        super().__init__(); self.width=WIDTH; self.height=85
    def draw(self):
        c=self.canv; c.setFillColor(NAVY); c.roundRect(0,0,WIDTH,85,8,stroke=0,fill=1)
        for x,big,small in [(20,'10','CHAPTERS'),(185,'70','LESSONS'),(340,'108','SOURCE ENTRIES')]:
            c.setFillColor(colors.white); c.setFont(B,25); c.drawString(x,43,big)
            c.setFillColor(colors.HexColor('#BCD3E3')); c.setFont(F,8); c.drawString(x,22,small)


class GuideDoc(BaseDocTemplate):
    def __init__(self,filename):
        super().__init__(filename,pagesize=A4,leftMargin=52,rightMargin=52,topMargin=54,bottomMargin=52,
                         title='Working With AI Agents',author='Adedaved',subject='An independent tutorial following IBM AI agents topics')
        self.addPageTemplates(PageTemplate(id='Guide',frames=[Frame(52,52,WIDTH,PAGE_H-106,id='body',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=self.decorate))
        self.chapter='Learning guide'; self.serial=0
    def beforeDocument(self):
        self.chapter='Learning guide'; self.serial=0
    def decorate(self,c,doc):
        c.saveState()
        if doc.page>1:
            c.setStrokeColor(colors.HexColor('#D6E2E9'));c.setLineWidth(.5);c.line(52,PAGE_H-34,PAGE_W-52,PAGE_H-34)
            c.setFont(F,7.8);c.setFillColor(MUTED);c.drawString(52,PAGE_H-26,'WORKING WITH AI AGENTS')
            c.drawRightString(PAGE_W-52,PAGE_H-26,'IBM topic learning path')
        c.setStrokeColor(colors.HexColor('#D6E2E9'));c.line(52,36,PAGE_W-52,36)
        c.setFont(F,7.5);c.setFillColor(MUTED);c.drawString(52,23,'Independent educational tutorial | Source snapshot: 14 Oct 2026')
        c.drawRightString(PAGE_W-52,23,str(doc.page));c.restoreState()
    def afterFlowable(self,flowable):
        if isinstance(flowable,Paragraph) and flowable.style.name in ('Chapter','Lesson'):
            text=flowable.getPlainText(); self.serial+=1; key=f'section-{self.serial}'
            self.canv.bookmarkPage(key)
            level=0 if flowable.style.name=='Chapter' else 1
            self.canv.addOutlineEntry(text,key,level=level,closed=False)
            if level==0:
                self.chapter=text
                if text not in ('Contents','How to use this guide'):
                    self.notify('TOCEntry',(0,text,self.page,key))


def markdown_flows(path, skip_title=True, lesson_number=None):
    lines=path.read_text().splitlines(); flows=[]; i=0
    while i<len(lines):
        line=lines[i].strip()
        if not line or (skip_title and line.startswith('# ')) or line.startswith('[Chapter overview]') or line.startswith('[Course home]'):
            i+=1;continue
        if line.startswith('The explanation and exercise are original educational writing.'):
            i+=1;continue
        if line.startswith('```'):
            code=[];i+=1
            while i<len(lines) and not lines[i].startswith('```'):
                code.append(lines[i]);i+=1
            # Code blocks are original prompts or local commands; wrap long display lines.
            import textwrap
            wrapped=[]
            for row in code: wrapped.extend(textwrap.wrap(row,width=91,replace_whitespace=False,drop_whitespace=False) or [''])
            flows.append(Preformatted('\n'.join(wrapped),STYLE['code']));i+=1;continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                row=[s.strip() for s in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?',s) for s in row): rows.append([P(s,'small',path.parent) for s in row])
                i+=1
            table=Table(rows,colWidths=[WIDTH/len(rows[0])]*len(rows[0]),repeatRows=1,hAlign='LEFT')
            table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),PALE),('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,0),.6,TEAL),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('LINEBELOW',(0,1),(-1,-1),.3,colors.HexColor('#D6E2E9'))]))
            flows.extend([table,Spacer(1,10)]);continue
        if line.startswith('## '):
            label=line[3:]
            if label=='IBM sources and implementation guides': label='Sources and next steps'
            if label=='Try it: original exercise': label='Try it - original exercise'
            flows.append(P(label,'h3'));i+=1;continue
        if line.startswith('- '): flows.append(P('• '+line[2:],'source' if '[S' in line else 'bullet',path.parent));i+=1;continue
        if re.match(r'\d+\. ',line): flows.append(P(line,'bullet',path.parent));i+=1;continue
        paragraph=[line];i+=1
        while i<len(lines) and lines[i].strip() and not re.match(r'#{1,3} |\d+\. |[-|]|```',lines[i].strip()):
            paragraph.append(lines[i].strip());i+=1
        flows.append(P(' '.join(paragraph),'body',path.parent))
    return flows


story=[]
story += [Spacer(1,55),P('PRACTICAL LEARNING GUIDE / 2026','label'),P('Working With<br/>AI Agents','title'),P('Understand the concepts.<br/>Direct the work. Review the result.','subtitle'),Spacer(1,12),CoverBand(),Spacer(1,28),P('A tutorial following IBM\'s ten topic groups, with original plain-English explanations, short exercises and answer checkpoints.'),P('Repository: [Adedaved/Working-With-AI-Agents](https://github.com/Adedaved/Working-With-AI-Agents)','small'),P('Source checked: 14 October 2026','small'),P('Independent educational writing. This guide is not an official IBM course or an IBM-endorsed publication.','small'),PageBreak()]
story += [P('How to use this guide','h1'),P('Read a concept, carry out its four-step exercise, and compare your interpretation with the answer checkpoint. Start with Chapters 1 and 2, then choose a workflow you can demonstrate and review.'),P('The conceptual lessons and synthetic exercises require no paid account. The local Python demo uses only the standard library. External IBM implementation guides may require software downloads, credentials or paid services; follow their current prerequisites.'),P('The working model','h3')]
model_rows=[['Part','What it supplies'],['Brain','Model-based reasoning and generation'],['Context and memory','Task information, state and retrieved sources'],['Workspace and tools','Places and capabilities for real actions'],['Feedback loop','Review, diagnosis and refinement']]
t=Table([[P(x,'small') for x in row] for row in model_rows],colWidths=[150,WIDTH-150])
t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),PALE),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9),('LINEBELOW',(0,0),(-1,-1),.3,colors.HexColor('#D6E2E9'))]))
story += [t,Spacer(1,14),P('What this guide demonstrates','h3'),P('The repository build validates chapter structure, source coverage, internal navigation, synthetic fixtures and a deterministic tool-call runtime example. Linked IBM cloud and framework labs are study resources and were not provisioned or executed during the build.'),P('How the source structure is preserved','h3'),P('All 108 linked entries in the ten instructional navigation groups map to a local chapter overview or lesson. Related explainers and labs share a lesson. Subjects repeated under Architecture and Multi-agent systems remain in both chapters with different emphasis.'),P('Version-sensitive topics','h3'),P('ACP is retained with IBM\'s notice that it merged into A2A. AutoGen and AG2 are distinguished. IBM\'s misspelled navigation label Agent gateaway is normalized to Agent gateway; the linked Bob MCP page redirects to Bob documentation.'),PageBreak(),P('Contents','h1')]
toc=TableOfContents();toc.levelStyles=[ParagraphStyle('TOC',fontName=F,fontSize=10.5,leading=18,textColor=INK,spaceBefore=7,leftIndent=0,firstLineIndent=0)]
story += [toc,Spacer(1,18),P('Use the PDF bookmarks to jump to individual lessons. Each lesson links to the corresponding IBM source and implementation guide. The source appendix includes visible URLs for standalone use.','small')]
for chapter in DATA['chapters']:
    story += [PageBreak(),P(f"CHAPTER {chapter['number']:02d}",'label'),P(f"{chapter['number']:02d}. {chapter['title']}",'h1'),P(chapter['objective'],'subtitle'),P(chapter['intro'])]
    if chapter['ids']:
        for sid in chapter['ids']:
            source=next(s for s in DATA['sources'] if s['id']==sid)
            story.append(P(f"Overview: [S{sid:03d}: {source['title']}]({source['url']})",'source'))
    for index,lesson in enumerate(chapter['lessons'],1):
        if index>1:
            story.append(PageBreak())
        lesson_flows=[P(f"{chapter['number']:02d}.{index:02d}  {lesson['title']}",'h2')]
        lesson_flows.extend(markdown_flows(ROOT/lesson['path']))
        story.append(KeepTogether(lesson_flows))
story += [PageBreak(),P('Appendix A. Workflow practice','h1')]
appendix_flows=markdown_flows(ROOT/'CAPSTONE_WORKFLOW.md')
for flow in appendix_flows:
    if isinstance(flow,Paragraph) and flow.style.name in ('Body','Bullet'):
        flow.style=ParagraphStyle('CompactAppendix',parent=flow.style,fontSize=9.4,leading=13.2,spaceAfter=5)
    elif isinstance(flow,Paragraph) and flow.style.name=='Section':
        flow.style=ParagraphStyle('CompactSection',parent=flow.style,spaceBefore=6,spaceAfter=4)
story.extend(appendix_flows)
story += [PageBreak(),P('Appendix B. Synthetic evaluation','h1'),P('These six records are teaching fixtures. The expected categories are a reviewed answer set, not the output of a live AI run. Keep the answers with the reviewer when evaluating an agent.'),P('Classification rules','h3')]
fixture=json.loads((ROOT/'05-lifecycle-and-operations/expected_ticket_results.json').read_text())
for name,rule in fixture['classification_rules'].items():story.append(P(f'**{name}:** {rule}'))
with (ROOT/'05-lifecycle-and-operations/example_tickets.csv').open(newline='') as stream: tickets=list(csv.DictReader(stream))
rows=[[P('Ticket','small'),P('Synthetic description','small'),P('Expected','small')]]
for ticket in tickets: rows.append([P(ticket['ticket_id'],'small'),P(ticket['description'],'small'),P(fixture['expected'][ticket['ticket_id']],'small')])
t=Table(rows,colWidths=[47,WIDTH-137,90],repeatRows=1)
t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),PALE),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),('LINEBELOW',(0,0),(-1,-1),.3,colors.HexColor('#D6E2E9'))]))
story += [t,Spacer(1,12),P('T004 requires clarification because the available information does not establish one of the defined categories. T006 remains email: the embedded request to override the rules is task data, not a trusted instruction.'),PageBreak(),P('Appendix C. Tool runtime example','h1'),P('The example below is original deterministic Python code. Its simulated request is written in the script; no model is called. It demonstrates the boundary between requesting a tool and validating and executing it.'),P('Run: `python3 02-components/tool_calling_demo.py`. Expected final line: `42`.','small')]
code=(ROOT/'02-components/tool_calling_demo.py').read_text()
import textwrap
wrapped=[]
for line in code.splitlines():wrapped.extend(textwrap.wrap(line,width=92,replace_whitespace=False,drop_whitespace=False) or [''])
story.append(Preformatted('\n'.join(wrapped),STYLE['code']))
story += [PageBreak(),P('Appendix D. IBM source index','h1'),P('The entries below map IBM\'s ten-group navigation to this tutorial. Some URLs recur because IBM places the same subject in more than one group. The referenced implementations remain on IBM\'s site. Checked: 14 October 2026.','small')]
for source in DATA['sources']:
    label=f"S{source['id']:03d}  {source['title']}"
    story.append(KeepTogether([P(label,'h3'),P(f"[{source['url']}]({source['url']})",'source'),P('Tutorial: '+source['local_path'],'small')]))
doc=GuideDoc(str(OUTPUT));doc.multiBuild(story)
print(str(OUTPUT))
