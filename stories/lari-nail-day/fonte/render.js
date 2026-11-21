const {chromium}=require('playwright');const S=process.argv[2];
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const n of ['01-cafe-mimo','02-preparo','03-esmaltacao','04-resultado-jelly','05-poa-aprovado']){
 await p.goto('file://'+S+'/st-'+n+'.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
 await p.screenshot({path:S+'/render/story-'+n+'.png'});}
await b.close();})();
