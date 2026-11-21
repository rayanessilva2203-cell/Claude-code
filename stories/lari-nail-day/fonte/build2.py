import sys
S=sys.argv[1]
star=lambda x,y,s:f'<svg class="star" style="left:{x}px;top:{y}px;width:{s}px;height:{s}px" viewBox="0 0 100 100"><use href="#st" fill="#fff"/></svg>'
E={'💗':'1f497','✨':'2728','⭐':'2b50','🌟':'1f31f','💖':'1f496','🥹':'1f979','🎀':'1f380','🌸':'1f338','☕':'2615','💅':'1f485','👍':'1f44d','💫':'1f4ab','🤍':'1f90d','🥰':'1f970','💕':'1f495','🙌':'1f64c'}
def t(s):
    for k,v in E.items(): s=s.replace(k,f'<img class="e" src="emoji/{v}.png">')
    return s
def em(ch,x,y,s,r=0): return f'<img class="em" src="emoji/{E[ch]}.png" style="left:{x}px;top:{y}px;width:{s}px;height:{s}px;transform:rotate({r}deg)">'
micro='<div class="micro"><span>NAIL DAY</span><b>Lari Rovira</b><span>NAIL DESIGNER</span></div>'
stories=[
 ('01-cafe-mimo','top',t('''<div class="blk" style="top:250px"><div class="script">começou o</div><div class="disp">nail day</div></div>
  <div class="blk" style="top:1560px"><div class="tag">dia de <u>retorno</u> com cafezinho ☕</div></div>''')
  +star(130,420,40)+star(940,1500,44)+em('💗',860,250,96,12)+em('✨',70,240,70)+em('🌸',60,1490,72,-10)),
 ('05-poa-aprovado','top',t('''<div class="blk" style="top:240px"><div class="script">1 mês depois</div><div class="disp m">nota 10 👍</div></div>
  <div class="blk" style="top:1420px"><div class="tag">foi assim que cheguei pro <u>retorno</u></div>
  <div class="imp">AINDA LINDAS 🥹✨</div></div>''')+star(80,300,48)+em('🌟',930,240,74,10)+em('💗',70,560,70,-12)),
 ('02-preparo','bot',t('''<div class="blk" style="top:1190px"><div class="script">paciência</div><div class="disp m">é o segredo</div>
  <div class="tag">cada cutícula no <u>tempinho dela</u></div>
  <div class="imp">SEM PRESSA, SEM DOR 🤍</div></div>''')+star(120,1200,52)+em('✨',900,1150,80)+em('💗',880,1690,66,14)),
 ('03-esmaltacao','bot',t('''<div class="blk" style="top:1170px"><div class="script">atenção</div><div class="disp m">aos detalhes</div>
  <div class="tag">ela escuta, explica e <u>capricha</u></div>
  <div class="imp">ATENDIMENTO DE AMIGA 💗</div></div>''')+star(950,1240,56)+em('⭐',80,1150,70,-8)+em('🎀',90,1680,70,-6)),
 ('04-resultado-jelly','top',t('''<div class="blk" style="top:270px"><div class="script">arrasou,</div><div class="disp">Lari!</div>
  <div class="tag">rosinha <u>glow</u> com cara de vidro</div></div>
  <div class="chip" style="left:70px;top:1470px;transform:rotate(-3deg)">amei demais 🥹💗</div>
  <div class="chip" style="right:70px;top:1600px;transform:rotate(2deg)">socorro, que lindo ✨</div>''')+star(140,400,40)+em('💖',850,280,96,12)+em('✨',470,1720,64)+em('🌸',880,1150,74,10)+star(900,1420,44)),
]
head=open(f'{S}/stories.html').read()
for i,(n,sh,body) in enumerate(stories,1):
    open(f'{S}/v2-{i}.html','w').write(head+f'<div class="s" style="background-image:url(out/{n}.jpg)"><div class="shade {sh}"></div>{micro}{body}</div></body></html>')
print('ok')
