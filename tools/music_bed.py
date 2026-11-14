"""Synthesised placeholder music bed (no model). python3 tools/music_bed.py <seconds> <out.wav>"""
import numpy as np, soundfile as sf, sys
sr=44100; bpm=100; beat=60/bpm; bar=4*beat
DUR=float(sys.argv[1]) if len(sys.argv)>1 else 38.4
def f(m): return 440*2**((m-69)/12)
# Am - F - C - G, two bars each
chords=[(45,[57,60,64,67]),(41,[57,60,65,69]),(48,[55,60,64,67]),(43,[55,59,62,67])]
n=int(DUR*sr); t=np.arange(n)/sr; L=np.zeros(n); R=np.zeros(n)
def env(x,a,r):
    e=np.ones(len(x)); na=int(a*sr); nr=int(r*sr)
    e[:na]=np.linspace(0,1,na)**2; e[-nr:]=np.linspace(1,0,nr)**2; return e
clen=2*bar; k=0; pos=0.0
while pos<DUR:
    root,notes=chords[k%4]; a=int(pos*sr); b=min(n,int((pos+clen+0.6)*sr)); tt=np.arange(b-a)/sr
    e=env(tt,1.2,1.2)
    for j,m in enumerate(notes):                      # pad: soft detuned sines
        for det,pan in((-0.004,0.3),(0.004,0.7)):
            w=np.sin(2*np.pi*f(m)*(1+det)*tt)+0.25*np.sin(2*np.pi*2*f(m)*(1+det)*tt)
            w*=e*0.055*(1+0.15*np.sin(2*np.pi*0.2*tt+j))
            L[a:b]+=w*(1-pan); R[a:b]+=w*pan
    bass=np.sin(2*np.pi*f(root)*tt)*e*0.16             # bass
    L[a:b]+=bass; R[a:b]+=bass
    arp=notes+[notes[1]+12,notes[2]]                   # pluck arpeggio, eighth notes
    for s in range(int(clen/(beat/2))):
        p=pos+s*beat/2; i=int(p*sr); d=int(0.5*sr)
        if i+d>n: break
        x=np.arange(d)/sr; m=arp[s%len(arp)]+12
        w=(np.sin(2*np.pi*f(m)*x)+0.3*np.sin(2*np.pi*2*f(m)*x))*np.exp(-x*9)*0.06
        pan=0.35+0.3*((s%2))
        L[i:i+d]+=w*(1-pan); R[i:i+d]+=w*pan
    for s in range(int(clen/beat)):                    # soft pulse on each beat
        p=pos+s*beat; i=int(p*sr); d=int(0.25*sr)
        if i+d>n: break
        x=np.arange(d)/sr; w=np.sin(2*np.pi*(55+60*np.exp(-x*30))*x)*np.exp(-x*18)*0.22
        L[i:i+d]+=w; R[i:i+d]+=w
    pos+=clen; k+=1
out=np.stack([L,R],1); fade=int(2.5*sr)
out[:fade]*=np.linspace(0,1,fade)[:,None]; out[-fade:]*=np.linspace(1,0,fade)[:,None]
out*=0.89/np.abs(out).max(); sf.write(sys.argv[2] if len(sys.argv)>2 else "bed.wav",out,sr)
