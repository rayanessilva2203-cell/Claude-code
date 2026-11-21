const {chromium}=require('playwright');const S=process.argv[2];
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const n of ['1','2','3','4','5']){await p.goto('file://'+S+'/v2-'+n+'.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
 await p.screenshot({path:S+'/render2/story-'+n+'.png'});}
await b.close();})();
