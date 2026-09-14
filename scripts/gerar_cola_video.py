"""Generate the concise five-minute recording guide and keep it in the repository."""
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output'/'pdf'/'cola-video-energia-observada.pdf'

def text(value):
    return value.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def main():
    OUT.parent.mkdir(parents=True,exist_ok=True)
    styles=getSampleStyleSheet()
    title=ParagraphStyle('title',parent=styles['Title'],fontName='Helvetica-Bold',fontSize=23,leading=28,textColor=colors.HexColor('#102c43'),spaceAfter=10)
    subtitle=ParagraphStyle('subtitle',parent=styles['Normal'],fontSize=10.5,leading=15,textColor=colors.HexColor('#416173'),spaceAfter=14)
    heading=ParagraphStyle('heading',parent=styles['Heading2'],fontName='Helvetica-Bold',fontSize=14,leading=18,textColor=colors.HexColor('#006d77'),spaceBefore=12,spaceAfter=6)
    body=ParagraphStyle('body',parent=styles['BodyText'],fontSize=9.4,leading=13.5,spaceAfter=5)
    cue=ParagraphStyle('cue',parent=body,backColor=colors.HexColor('#edf7f6'),borderColor=colors.HexColor('#72b7b2'),borderWidth=.5,borderPadding=7,spaceBefore=4,spaceAfter=8)
    warn=ParagraphStyle('warn',parent=body,backColor=colors.HexColor('#fff3d6'),borderColor=colors.HexColor('#d69e2e'),borderWidth=.5,borderPadding=7,spaceBefore=4,spaceAfter=8)
    doc=SimpleDocTemplate(str(OUT),pagesize=A4,rightMargin=1.55*cm,leftMargin=1.55*cm,topMargin=1.35*cm,bottomMargin=1.25*cm)
    story=[Paragraph('Cola de vídeo - Energia Observada',title),Paragraph('Duração total: 5 minutos. Caso real: JUREMA (13317), julho de 2026. Use a interface atual em http://localhost:8504.',subtitle)]
    rows=[['Tempo','Clique / mostre','Fale'],
      ['0:00-1:00','Câmera','“Oi, eu sou o Pedro. Vou mostrar uma solução para priorizar investigações usando dados públicos da ANEEL. Sem uma ferramenta, o analista compara milhões de registros mês a mês e decide no olho. A fila e o Dossiê tornam essa decisão explicável e rastreável.”'],
      ['1:00-2:30','Fila; apontar para JUREMA e aviso da amostra','“Esta tela mostra quatro conjuntos da Companhia Energética do Ceará, em julho de 2026. A fila é ordenada por variação absoluta de afetações reportadas. JUREMA aparece primeiro: 729 registros atuais contra 635 anteriores, com diferença absoluta de 259.038 afetações. O aviso informa que este é um recorte de demonstração, não cobertura nacional.”'],
      ['2:30-3:30','Abrir Dossiê de JUREMA; mostrar indicadores e exportação','“O Dossiê explica o destaque com indicadores, histórico e confiança documental. A exportação gera dossie.md, registros.csv e manifesto.json. O pacote pode ser verificado depois contra alterações nos arquivos exportados.”'],
      ['3:30-4:15','Mostrar avisos e limitações','“O sistema não afirma causa. O município localiza o equipamento e não delimita necessariamente os consumidores afetados. Afetações reportadas não são consumidores únicos, e ausência de dados não equivale a ausência de interrupções.”'],
      ['4:15-5:00','Câmera,'“A ANEEL atualiza a base mensalmente. O processo ingere, valida e publica uma nova versão somente quando os dados estão consistentes, preservando a versão anterior em caso de falha. O resultado é uma triagem repetível, com evidência que sustenta a próxima investigação.”'],
      ['','',''],
      ['','',''],
      ['','',''],
      ['','',''],
      ['','','']]
    table=Table([[Paragraph(text(cell),body) for cell in row] for row in rows],colWidths=[2.05*cm,4.0*cm,10.0*cm],repeatRows=1)
    table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#102c43')),('TEXTCOLOR',(0,0),(-1,0),colors.white),('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('VALIGN',(0,0),(-1,-1),'TOP'),('GRID',(0,0),(-1,-1),.35,colors.HexColor('#b8c7d0')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f4f8fa')]),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
    story += [table,Spacer(1,8),Paragraph('<b>Antes de gravar</b>: confirme que a fila, JUREMA e o Dossiê estão visíveis na interface.',cue),Paragraph('<b>Não diga</b>: que o produto provou a causa, que há cobertura nacional neste recorte ou que afetações são consumidores únicos.',warn)]
    def page(canvas,doc):
        canvas.saveState(); canvas.setStrokeColor(colors.HexColor('#72b7b2')); canvas.line(1.55*cm,1.0*cm,A4[0]-1.55*cm,1.0*cm); canvas.setFont('Helvetica',8); canvas.setFillColor(colors.HexColor('#416173')); canvas.drawString(1.55*cm,.65*cm,'Energia Observada | cola de gravação'); canvas.drawRightString(A4[0]-1.55*cm,.65*cm,f'Página {doc.page}'); canvas.restoreState()
    doc.build(story,onFirstPage=page,onLaterPages=page)
    print(OUT)

if __name__=='__main__': main()


