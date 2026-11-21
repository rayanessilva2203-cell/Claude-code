import sys
S=sys.argv[1]
star=lambda x,y,s:f'<svg class="star" style="left:{x}px;top:{y}px;width:{s}px;height:{s}px" viewBox="0 0 100 100"><use href="#st" fill="#fff"/></svg>'
micro='<div class="micro"><span>NAIL DAY</span><b>Lari Rovira</b><span>NAIL DESIGNER</span></div>'
stories=[
 # 1 capa
 ('01-cafe-mimo','top',f'''<div class="blk" style="top:250px"><div class="script">começou o</div><div class="disp">nail day</div></div>
  <div class="blk" style="top:1560px"><div class="tag">com cafezinho e <u>mimo</u> na mesa ☕</div></div>
  {star(870,260,64)}{star(130,420,40)}{star(940,1500,44)}'''),
 # 2 paciência
 ('02-preparo','bot',f'''<div class="blk" style="top:1210px"><div class="script">o segredo?</div><div class="disp">paciência</div>
  <div class="tag">cutícula feita <u>sem pressa</u> e sem dor</div>
  <div class="imp">CUIDADO NÍVEL LARI ✦</div></div>{star(120,1230,56)}{star(900,1180,40)}'''),
 # 3 atenção
 ('03-esmaltacao','bot',f'''<div class="blk" style="top:1150px"><div class="script">atenção em</div><div class="disp m">cada detalhe</div>
  <div class="tag">ela escuta, explica e <u>capricha</u></div>
  <div class="imp">ATENDIMENTO DE AMIGA 💗</div></div>{star(70,1120,48)}{star(950,1250,60)}'''),
 # 4 resultado
 ('04-resultado-jelly','top',f'''<div class="blk" style="top:330px"><div class="script">socorro,</div><div class="disp">que unha</div>
  <div class="tag">rosinha <u>glow</u> com cara de vidro</div>
  <div class="imp">CLOSE CERTO 🌸</div></div>{star(860,300,62)}{star(140,420,40)}
  <div class="chip" style="right:60px;top:1560px">acabamento <i>de vitrine</i> ✦</div>'''),
 # 5 CTA
 ('05-poa-aprovado','top',f'''<div class="blk" style="top:250px"><div class="script">aprovadíssima</div><div class="disp m">nota 10 👍</div></div>
  {star(80,300,48)}{star(950,380,40)}
  <div class="blk" style="top:1380px"><div class="tag">quer uma unha <u>divônica</u> assim?</div><br>
  <div class="cta">agenda com a <span>Lari</span> 💅</div></div>'''),
]
head=open(f'{S}/stories.html').read()
for n,sh,body in stories:
    html=head+f'<div class="s" style="background-image:url(out/{n}.jpg)"><div class="shade {sh}"></div>{micro}{body}</div></body></html>'
    open(f'{S}/st-{n}.html','w').write(html)
print('ok')
