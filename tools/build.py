import re, sys
svg = open('tina_bird_logo.svg').read()
P = re.findall(r'<path d="([^"]+)"', svg)
R, K = '#e73519', '#111111'
def p(d, fill, extra=''): return f'<path d="{d}" fill="{fill}" fill-rule="evenodd"{extra}/>'
# fleck fly-out vectors (viewBox units)
fl = [(30,-40),(70,-30),(50,-80),(90,-10),(40,-60),(80,-50)]
flecks = ''.join(p(P[i], R, f' class="fk" style="--i:{i};--fx:{fl[i][0]}px;--fy:{fl[i][1]}px"') for i in range(6))
out = ('<svg viewBox="190 236 740 930" xmlns="http://www.w3.org/2000/svg">'
  '<g class="lg-letters">'
  f'<g class="l" style="--i:0">{p(P[12],K)}</g>'
  f'<g class="l" style="--i:1">{p(P[9],K)}</g>'
  f'<g class="l" style="--i:2">{p(P[10],K)}{p(P[8],K)}</g>'
  f'<g class="l" style="--i:3">{p(P[11],K)}</g>'
  '</g>'
  f'<g class="lg-bird">{p(P[7],R)}{p(P[6],R," class=\"lg-eye\"")}<g class="lg-flecks">{flecks}</g></g>'
  '</svg>')
src = open('index.src.html').read()
open('index.html','w').write(src.replace('{{LOGO_SVG}}', out))
print(len(P), 'paths; index.html', len(src)+len(out))
