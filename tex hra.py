import random
while True:
 print("Zdravím poutníku. Probudil jsi se někde v bludišti a musíš najít cestu ven. Ale nebude to jen tak. Hodně štěstí.")
 a=input("Kam půjdeš? (vlevo)*(vpravo) ")

 if a=="vlevo":
     print("Před tebou je nápis: kolik je ((44/5)-6,8)^2")
     print("Pod příkladem jsou tlačítka (4)*(598).")
     b=input("Které zmáčkneš? (4)*(598)")
     if b=="4":
         print("Zeď se otevřela a před tebou jsou dvě cesty.")
         c=input("Kam půjdeš? (vlevo)*(rovně)")
         if c=="vlevo":
             print("Objevil jsi další rozcestí.")
             f=input("Kam půjdeš? (vpravo)*(rovně)")
             if f=="vpravo":
                 print("Slepá. Za tebou se zavřely dveře a místnost se zaplnila vodou. Zemřel jsi!")
             elif f=="rovně":
                 print("Narazil jsi na schody dolů a nahoru. Vedle schodů nahoru byl klíč.")
                 g=input("Kam jsi šel po tom co jsis vzal klíč? (nahoru)*(dolů)")
                 if g=="nahoru":
                     print("Po hodině cesty do shodů jsi si všiml, že shody za tebou postupn mizí, ale před tebou už nejsou žádné. Zemřel jsi!")
                 elif g=="dolů":
                     print("Zakopl jsi a zkutálel jsi se ze schodů. Před tebou jsou dveře.")
                     h=input("Co uděláš? (odemču)*(zdřímnu si)")
                     if h=="odemču":
                         print("Za dveřmi je kostra, která k tobě má obě ruce nastavené k potřesení.")
                         i=input("Kterou rukou z tvého pohledu mu potřeseš? (pravou)*(levou)")
                         if i=="pravou":
                             print("Ozval se smích a kostra ti utrhla ruku. Zemřel jsi!")
                         elif i=="levou":
                             print("Z pusy mu vyjel papírek.")
                             print("Na papírku je napsáno: 01111010 01101101 01101001 01111010")
                             print("Vylušti kód a řekni ho nahlas. Ale pozor máš jen jeden pokus.")
                             j=input("Jak tedy zní překlad?")
                             if j=="zmiz":
                                 print("Kostra se zasunula do země a ty jsi prošel dál.")
                                 print("Došel jsi k rozcestí")
                                 k=input("Kam se vydáš? (vlevo)*(rovně)*(vpravo)")
                                 if k=="vlevo":
                                     print("Narazil jsi na truhlu")
                                     l=input("Co uděláš? (otevřu ji)*(půjdu dál)")
                                     if l=="otevřu ji":
                                         print("Našel jsi papírek s heslem,které bude důležité. Na papírku je napsáno:AK11J89")
                                         print("Šel jsi dál a došel jsi k rozcestí.")
                                         m=input("Kam půjdeš? (vpravo)*(vlevo)")
                                         if m=="vpravo":
                                             print("Stoupnul jsi na past a ta ti prostřelila hruď šípem. Zemřel jsi!")
                                         elif m=="vlevo":
                                             print("Narazil jsi na rytíře, který se zeptal na heslo.")
                                             n=input("Co mu řekneš?")
                                             if n=="AK11J89":
                                                 print("Rytíř ti ustoupil a ty můžeš projít.")
                                                 o=input("Jsi na rozcestí. Kam půjdeš? (vlevo)*(vpravo)")
                                                 if o=="vlevo":
                                                     print("Propadl ses. Zemřel jsi!")
                                                 elif o=="vpravo":
                                                     print("Zpadl na tebe strop. Zemřel jsi!")
                                                 else:
                                                     print("Napsal jsi špatný příklad")
                                             else:
                                                 "Rytíř zařve a setne ti hlavu. Zemřel jsi!"
                                         else:
                                             print("Napsal jsi špatný příklad")
                                     elif l=="půjdu dál":
                                         print("Narazil jsi na rytíře, který se tě zeptal na heslo.")
                                         print("Heslo neznáš a tak ti setne hlavu. Zemřel jsi!")
                                     else:
                                         print("Napsal jsi špatný příklad")
                                 elif k=="rovně":
                                     print("Narazil jsi na staříka v kápi a ten ti dal hádanku.")
                                     print("Je to bílé, sladké a křupavé.")
                                     p=input("Co je to? ")
                                     if p=="cukr":
                                         print("Stařík se pousmál a vytáhl ti most aby jsi se dostal přez propast.")
                                         print("Před tebou se zjeví duch, který ti chce říct cestu.")
                                         q=input("Co uděláš? (vyslechnu ho)*(odmítnu ho)")
                                         if q=="vyslechnu ho":
                                             print("Duch povídá:vprava-pozor rovně-vpravo-vlevo-rovně-dveře<1234>")
                                             print("Vtom se objeví druhý duch, který ti řekne, že už je pozdě, protože toto je slepá ulička.")
                                             print("První duch příšel pozdě. Tato trasa funguje až po deváté zastávce.")
                                             print("Duchové tě chytili a zhodili do propasti.")
                                         elif q=="odmítnu ho":
                                             print("Došel jsi na rozcestí")
                                             r=input("kam půjdeš? (vlevo)*(vpravo)")
                                             if r=="vlevo":
                                                 print("Vidíš světlo. Podíval jsi se dovnitř a světlo ti vypálilo oči. Zemřel jsi!")
                                             elif r=="vpravo":
                                                 print("Narazil jsi na stádo hladových prasat a ta tě sežrala. Zemřel jsi!")
                                             else:
                                                 print("Napsal jsi špatný příklad")
                                         else:
                                             print("Napsal jsi špatný příklad")
                                     else:
                                         print("Stařík se zamračíl, chytil tě hákem a zhodil tě do propasti. Zemřel jsi!")
                                 elif k=="vpravo":
                                     print("Narazil jsi na další rozcestí")
                                     s=input("Kam půjdeš? (vpravo)*(rovně)")
                                     if s=="vpravo":
                                         print("Odřel jsi se o zeď a do krve se ti dostal jed. Zemřel jsi!")
                                     elif s=="rovně":
                                         print("Vidíš dlouhou chodbu a před ní dva kameny.")
                                         t=input("Co uděláš? (projdu)*(hodím kámen)")
                                         if t=="projdu":
                                             print("Vešel jsi do chodby. V chodbě byla nastražená past. Zemřel jsi!")
                                         elif t=="hodím kámen":
                                             print("Kámen aktivoval past. Hodil jsi i druhý, ale už se nic nestalo.")
                                             print("Prošel jsi ke dveřím kde byly dva symboly. Býk a Orel")
                                             print("Nad nimy byl nápis:Koho jsi potkal?")  
                                             u=input("Který symbol zmáčkneš? (býk)*(orel)")
                                             if u=="býk":
                                                 print("Dveře se otevřely a ty vidíš dvě cesty.")
                                                 v=input("Kam půjdeš? (vlevo)*(vpravo)") 
                                                 if v=="vlevo":
                                                     print("Objevil jsi dvě tlačítka")
                                                     w=input("Které zmáčkneš? (exit)*(konec)")
                                                     if w=="exit":
                                                         print("Pod tebou se otevřel poklop a ty jsi se propadl. Zemřel jsi!")
                                                     elif w=="konec":
                                                         print("Pod tebou se otevřel poklop a ty jsi se propadl. Zemřel jsi!")
                                                     else:
                                                         print("Napsal jsi špatný příklad")
                                                 elif v=="vpravo":
                                                     print("Jdeš temnou uličkou a najdenou na levé straně světlo.")
                                                     x=input("Kam půjdeš? (rovně)*(vlevo)")
                                                     if x=="rovně":
                                                         print("Zakopl jsi a rozbil sis hlavu. Zemřel jsi!")
                                                     elif x=="vlevo":
                                                         print("Před tebou je dlouhá ulička")
                                                         print("Objevil jsi truhlu.")
                                                         y=input("Co uděláš? (otevřu ji)*(půjdu dál)")
                                                         if y=="otevřu ji":
                                                             print("Byla to past a truhla vybouchla. Zemřel jsi!")
                                                         elif y==("půjdu dál"):
                                                             print("Došel jsi ke dveřím na kterých visí zámek na čtyřmístný kód.")
                                                             print("na zemi leží papírek, na kterém je napsáno: ((9+8)^2+(25-5,5))*2^2")
                                                             z=input("Jaký je kód? ")
                                                             if z=="1234":
                                                                 print("Dveře se otevřeli a ty vejdeš do oslepujícíjo světla. V tom slyšíš poplach.")
                                                                 print("Najednou otevřeš očí a vidíš svůj budík jak zvoní u postele a ty nejsi schopný na nic, než říct jen zmatené: Co!?")
                                                             else:
                                                                 print("Napsal jsi špatný příklad")
                                                         else:
                                                             print("Napsal jsi špatný příklad")
                                                     else:
                                                         print("Napsal jsi špatný příklad") 
                                                 else:
                                                     print("Napsal jsi špatný příklad")                                              
                                             elif u=="orel":
                                                 print("Otočil jsi se a viděl obrovského orla, který ti uklovnul hlavu. Zemřel jsi!")
                                             else:
                                                 print("Napsal jsi špatný příklad")                                           
                                         else:
                                             print("Napsal jsi špatný příklad")
                                     else:
                                         print("Napsal jsi špatný příklad")
                                 else:
                                     print("Napsal jsi špatný příklad")
                             else:
                                 print("Okolo se rozezněl smích a místnost se zaplnila vodou. Zemřel jsi!")
                         else:
                             print("Napsal jsi špatný příklad")
                     elif h=="zdřímnu si":
                         print("Zpadla na tebe louče. Zemřel jsi!")
                     else:
                         print("Napsal jsi špatný příklad")
                 else:
                     print("Napsal jsi špatný příklad") 
             else:
                print("Napsal jsi špatný příklad")
         elif c=="rovně":
             print("Stojí před tebou minotaur.")
             d=input("Co uděláš? (napadnu ho)*(uteču)*(rozesměju ho)")
             if d=="napadnu ho":
                 print("Zlomil jsi si ruku a minotaur ti utrhl nohy. Zemřel jsi!")
             elif d=="uteču":
                 print("Minotaur tě dohnal a rozdrtil ti hrudník. Zemřel jsi!")
             elif d=="rozesměju ho":
                 print("Rozptýlil jsi ho a proplížil jsi se kolem něho.")
                 e=input("Před tebou je rozcestí. Kam se vydáš? (vpravo)*(vlevo)")
                 if e=="vpravo":
                     print("Slepá. Minotaur tě probodl. Zemřel jsi!")
                 elif e=="vlevo":
                     print("Slepá. Minotaur tě probodl. Zemřel jsi!")   
                 else: 
                     print("Napsal jsi špatný příklad") 
             else:
                 print("Napsal jsi špatný příklad")           
         else:
             print("Napsal jsi špatný příklad")
     elif b=="598":
         print("Zdi se začaly zavírat a pomalu tě rozmáčly. Zemřel jsi!")
     else:
         print("Napsal jsi špatný příklad")
 elif a== "vpravo":
     print("Zakopl jsi a spadl propasti plné dřevěných kůlů. Zemřel jsi!")
 else:
     print("Napsal jsi špatný příklad")

 znovu = input("Chceš hrát znovu? (reset) ")

 if znovu.lower() == "reset":
     continue
 else:
     break