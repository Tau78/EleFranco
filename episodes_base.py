"""Episodi 1–21 — sorgente testi editabile. Modifica qui e rigenera con aggiorna_libro.py."""

from __future__ import annotations

INTRO = 'Le Avventure di EleFranco Franchini STAGIONE 1 - EDIZIONE COMPLETA UNIFICATA V11 Iris Edition "C’è una magia segreta nel cammino di un elefante: ogni volta che EleFranco Franchini esce per un piccolo impegno, il destino gli mette accanto un amico da aiutare. E così, tra un gesto gentile e un sorriso inaspettato, la missione si compie da sola, perché chi semina bontà ritrova sempre la strada di casa."'

BASE_EPISODES: list[dict] = [
    {"num": 1,
        "title": '🎉 La Festa e il Castoro Fred 🦫',
        "missione": 'EleFranco deve andare al supermercato a comprare festoni e nastri per la Festa della sua amica Franca. 🎉',
        "incontro": "Incontra Fred il Castoro, disperato in riva al fiume perché la sua diga continua a crollare e l'acqua sta per allagare la tana dei suoi amici scoiattoli. 🪵",
        "aiuto": 'EleFranco fa da scudo alla corrente e impasta del fango argilloso con la proboscide per cementare la diga, sporcandosi tantissimo dalla testa ai piedi. 🟤',
        "morale": 'Aiutare gli altri protegge la comunità. 🤝',
        "colpo": 'Il fango asciugandosi crea decorazioni bellissime come i festoni di una Festa. Gli scoiattoli riconoscenti gli regalano un enorme pacco di nastri colorati e dolci di noci per la Festa. 🐿',
        "finale_schema": 'La missione è compiuta senza entrare al supermercato! E via di risata: OH... OH... OH...',
        "racconto": """C'era una volta un Elefante di nome Franco, che gli amici chiamavano ... EleFranco. Di cognome faceva Franchini, un dettaglio molto importante per un cittadino così illustre!

Abitava in una graziosa e accogliente casa alla periferia di FrancaVilla, un piccolo e tranquillo paesino circondato dal verde, un luogo incantevole dove i tetti delle case sembravano fatti di marzapane, i camini sbuffavano nuvole a forma di ciambella e l'aria profumava sempre di zucchero a velo e pane appena sfornato. EleFranco era grande, grosso e immensamente generoso, con un simpatico ciuffetto di capelli neri sulla testa che ballava a ogni suo passo.

Quel mattino il suo stomaco emise un brontolio pazzesco, ma c'era qualcosa di più importante del suo appetito: «Oggi è la Festa della mia cara amica Franca!» si disse, controllando la dispensa vuota. «Devo correre al supermercato a comprare i festoni più belli di tutti. Niente decorazioni, niente Festa!» Si infilò i suoi stivali giganti di cuoio marrone, lucidati per l'occasione, aprì la porta di casa e si mise in cammino verso il centro. Mentre avanzava sulla strada sterrata, la terra tremava dolcemente al ritmo dei suoi piedoni: THUMP THUMP THUMP.

Arrivato vicino al ponticello sul fiume, notò una gran confusione. Sulla riva, un castoro dalla pelliccia lucida e dai grandi denti color avorio correva avanti e indietro tenendosi la testa tra le zampe. Era Fred il Castoro, il più bravo costruttore di tutta FrancaVilla, e quella mattina piangeva disperato.

«EleFranco, è una catastrofe!» singhiozzò Fred. «Stanotte è arrivata una corrente improvvisa e la mia diga sta cedendo! Se crolla del tutto, l'acqua allagherà la mia tana e perfino l'albero-casa degli scoiattoli che dormono là sotto. Ho lavorato per mesi a quei tronchi e ora si sfaldano come grissini!»

«Respira, Fred,» disse EleFranco con voce calda come una coperta al sole. «Ci sono qui io adesso.»

Ma poi, guardando l'acqua, la sua mente cominciò a vagare. Iniziò a pensare a quanto fosse tardi, a quanti festoni e nastri ci fossero al supermercato — rossi o dorati? — e quanti coriandoli mettere per la Festa di Franca.

Stava quasi per perdersi del tutto in quei pensieri golosi quando Fred lanciò un urlo lacerante: «EleFranco, sta crollando TUTTO!»

Allora l'elefante scosse le grandi orecchie e disse ad alta voce la sua parola magica: "FOCUS!"

«Tieni duro, Fred, la tua diga la salviamo insieme!» gridò, e in un attimo passò all'azione. Entrò nel fiume con un tonfo gigantesco e piantò le sue zampe massicce contro la corrente, usandole come un enorme scudo che spezzava la forza dell'acqua. Poi, con la proboscide, cominciò a scavare il fango argilloso dal fondo del fiume e a impastarlo con cura sui rami sconnessi della diga, tappando ogni falla.

Lavorò senza fermarsi mai, mentre Fred gli passava rametti e foglie. «Un po' più a destra! Ecco, lì! Sei fortissimo!» lo incoraggiava il castoro. Pezzo dopo pezzo, la diga tornò solida come una muraglia. Ma EleFranco si era coperto di melma marrone dalla punta del ciuffo alla coda: sembrava una statua di cioccolato.

«Oh no,» mormorò guardandosi. «Sono troppo sporco per entrare al supermercato, e la Festa di Franca sta per cominciare. Le ho rovinato le decorazioni...»

Mentre si disperava, il sole caldo del mezzogiorno cominciò ad asciugare il fango sulla sua pelle. E successe una cosa incredibile: l'argilla seccando si crepò in mille motivi geometrici eleganti, ghirigori e fiorellini, proprio come i festoni di una Festa monumentale! In quello stesso momento, gli scoiattoli salvati sbucarono festanti dai rami, reggendo a fatica un vassoio dondolante con un enorme pacco di nastri colorati e dolci di noci per la Festa, caldi e profumati.

«Per te, EleFranco! Hai salvato la nostra casa!» squittirono in coro.

La missione era compiuta senza nemmeno entrare nel negozio: Franca avrebbe avuto la Festa più bella del mondo!

EleFranco alzò la proboscide al cielo e scoppiò nella sua famosa risata: OH... OH... OH...""",
    },
    {"num": 2,
        "title": "👓 La Visita dall'Oculista e Jack il Geco 🦎",
        "missione": "EleFranco deve andare dall'oculista perché vede un po' sfocato e deve misurare la vista. 👁",
        "incontro": "Sente piangere Jack il Geco, che ha perso i suoi minuscoli occhiali da sole nell'erba alta e non riesce più a cacciare le mosche. 🌿",
        "aiuto": 'EleFranco si mette a terra e fa "l\'aspirapolvere" con la proboscide. Lo sforzo di mettere a fuoco oggetti così piccoli nell\'erba fa fare una ginnastica pazzesca ai suoi occhi. 🔍',
        "morale": 'Per vedere le cose grandi, bisogna fare attenzione a quelle piccolissime. ❤',
        "colpo": 'Ritrova gli occhialini sulla punta della proboscide. Quella ginnastica oculare intensiva gli ha curato completamente la vista sfocata. 🎉',
        "finale_schema": "Non c'è più bisogno dell'oculista! Risata: OH... OH... OH...",
        "racconto": """C'era una volta un Elefante di nome Franco, che gli amici chiamavano ... EleFranco. Di cognome faceva Franchini!

Abitava nella sua bella casa nel paesino di FrancaVilla, un borgo magico abbarbicato sulla roccia di una montagna, dove i vialetti profumavano di menta selvatica, le casette si aggrappavano ai dirupi come nidi di rondine e il vento di montagna suonava arpe invisibili tra le fronde degli alberi.

Quella mattina, però, il mondo intorno a lui sembrava fatto di nuvole sfocate. Gli alberi del giardino erano grandi macchie verdi tremolanti e non riusciva nemmeno a distinguere il colore dei fiori sul davanzale. «Ahi ahi, qui non ci vedo più nulla,» borbottò strofinandosi gli occhi con la punta della proboscide. «Devo proprio andare dal vecchio gufo oculista, dall'altra parte del paese, a farmi misurare la vista.» Si infilò le sue scarpe giganti da passeggio con i lacci colorati e uscì di casa, camminando piano e con grande attenzione per non inciampare. Ad ogni passo prudente il sentiero roccioso risuonava: THUMP THUMP THUMP.

Mentre passava vicino a un muretto di pietra, sentì un flebile pianto provenire dall'erba alta. Si chinò, strizzò gli occhi e a fatica mise a fuoco una piccola sagoma: era Jack il Geco, un rettile dalla pelle verdissima e brillante, con le dita a ventosa e due grandi occhi rotondi colmi di lacrime.

«Che disastro, EleFranco!» piagnucolò Jack. «Un colpo di vento mi ha portato via i miei occhiali da sole scuri, quelli minuscoli! Senza non riesco a cacciare le mosche, perché il riflesso del sole sulla roccia mi acceca all'istante. Sono finiti da qualche parte in questo mare d'erba e io non li trovo più!»

«Non temere, piccolo Jack, due occhi in più non guastano mai,» rispose EleFranco con dolcezza.

Ma poi si mise a fissare il prato e, complice la vista annebbiata, vide solo un'immensa distesa confusa. La sua mente prese a vagare: iniziò a pensare a quanti tipi di lenti colorate esistessero, se l'oculista gli avrebbe fatto provare degli occhiali giganti cerchiati di rosso e se gli sarebbero stati bene sul nasone.

Si stava perdendo in queste fantasie quando Jack singhiozzò più forte: «EleFranco, ho fame e non vedo nulla!»

Allora l'elefante scosse la testa e gridò la sua parola magica: "FOCUS!"

«Tranquillo, Jack, i tuoi occhiali li ritroviamo subito,» lo rassicurò.

Si inginocchiò sull'erba e usò la proboscide come un potente aspirapolvere, risucchiando l'aria dal terreno con delicatezza per non aspirare gli insetti. Per controllare cosa restasse impigliato tra le pieghe della pelle, sforzò al massimo i muscoli degli occhi: stringeva e allargava le pupille, le metteva a fuoco vicino e poi lontano, cercando i dettagli più minuscoli tra i fili d'erba. Era una vera e propria ginnastica oculare.

«Vedo qualcosa che luccica! No... era una goccia di rugiada,» diceva, continuando a strizzare e spalancare gli occhi. Ripeté quel movimento decine di volte, finché i suoi occhi non cominciarono a lavorare come ingranaggi ben oliati.

All'improvviso — clack! — il mondo tornò perfettamente nitido. E la sorpresa fu doppia: gli occhialini di Jack erano proprio lì, appoggiati sulla punta del suo nasone, mentre quella ginnastica intensiva aveva riabilitato del tutto i suoi occhi! La vista sfocata era sparita, gli alberi avevano di nuovo contorni precisi e i fiori erano rossi, gialli e viola.

«Ci vedo benissimo!» esultò EleFranco, mentre Jack si rimetteva gli occhialini e schizzava via felice a caccia di mosche. La missione era compiuta e dell'oculista non c'era più bisogno.

Felice, EleFranco partì con la sua conosciutissima risata: OH... OH... OH...""",
    },
    {"num": 3,
        "title": '🍌 Dal Fruttivendolo e Raffa la Giraffa 🦒',
        "missione": 'EleFranco va dal fruttivendolo a comprare un casco di banane per la merenda. 🧺',
        "incontro": 'Incontra Raffa la Giraffa che ha un terribile torcicollo e non riesce a piegare la testa per bere alla fontanella. ⛲',
        "aiuto": "EleFranco riempie la proboscide d'acqua fresca e fa un idromassaggio tiepido sul collo di Raffa per sciogliere il nodo. Lo sforzo gli fa venire una fame da lupi. 😋",
        "morale": 'Il sollievo di un amico vale più di qualsiasi pancia piena. 🦒',
        "colpo": "Raffa, guarita, si allunga verso l'alto e stacca da un albero altissimo un casco di banane selvatiche giganti e dolcissime per regalarlo a EleFranco. 🌳",
        "finale_schema": 'Banane fresche e gratis! Risata: OH... OH... OH...',
        "racconto": """C'era una volta un Elefante di nome Franco, che gli amici chiamavano ... EleFranco. Di cognome faceva Franchini.

Abitava nella sua accogliente casa all'interno del paesino di FrancaVilla, un borgo adagiato su dolci colline dorate, dove i ruscelli scorrevano limpidi cantando ninne nanne, l'erba dei prati brillava al sole come un immenso tappeto di smeraldi e i meli profumavano l'aria del mattino.

Era un pomeriggio caldo, di quelli che fanno venire una voglia matta di qualcosa di fresco. EleFranco frugava nella sua grande cesta della frutta, ma trovò solo qualche guscio di nocciolina vuoto. «Accidenti!» esclamò, mentre lo stomaco gli lanciava un brontolio sonoro. «Il mio regno per un casco di banane! Gialle, mature e profumate... ecco cosa mi serve per la merenda.» Si infilò i suoi stivali giganti e si diresse verso il centro, dove c'era la bottega del fruttivendolo Pino. Camminando lungo la via principale, il selciato risuonava sotto i suoi piedoni: THUMP THUMP THUMP.

Vicino alla piazza principale, EleFranco vide qualcosa di stranissimo. C'erano due zampe lunghissime e un corpo coperto di macchie color caramello, ma il collo, invece di salire dritto verso il cielo, era piegato a metà e penzolava molle come un ombrello dimenticato sotto la pioggia. Era Raffa la Giraffa, e i suoi grandi occhi dalle lunghe ciglia erano pieni di lacrime.

«Oh, EleFranco, che tormento!» mugolò Raffa con un filo di voce. «Stamattina mi sono svegliata con un torcicollo terribile, un nodo durissimo proprio qui. Non riesco più a piegare il collo per bere alla fontanella e ho una sete da morire! Più provo ad abbassarmi, più mi fa male.»

«Povera Raffa, ora ci penso io,» rispose subito EleFranco, posandole una zampa gentile sul fianco.

Ma poi i suoi occhi caddero sulle vetrine colorate della piazza e la mente prese il volo: cominciò a pensare a quante banane avrebbe comprato, se intere o tagliate a rondelle nel latte, dimenticandosi per un istante della povera giraffa.

Si stava distraendo, ma vedendo Raffa piangere in silenzio, scosse le grandi orecchie e gridò: "FOCUS!"

«Niente paura, amica mia, quel nodo lo sciogliamo subito,» le promise.

Corse alla fontanella comunale e aspirò una lunga sorsata d'acqua con la proboscide. La tenne in bocca qualche istante per intiepidirla, perché l'acqua troppo fredda avrebbe fatto male ai muscoli indolenziti di Raffa. Poi tornò dall'amica e cominciò a spruzzarle un perfetto idromassaggio termico lungo tutto il collo, dall'alto verso il basso, con getti dolci e regolari.

«Ooooh, che meraviglia,» sospirò Raffa mentre EleFranco massaggiava con la punta della proboscide i punti più rigidi. «Sento che si scioglie... continua, ti prego!» L'elefante insistette pazientemente finché non sentì un piccolo "pop" muscolare: il nodo si era sciolto e il collo di Raffa tornò a issarsi dritto e fiero verso il cielo.

EleFranco era affamatissimo dopo tutto quello sforzo, ma vedere l'amica di nuovo felice gli riempiva il cuore più di qualsiasi merenda. Raffa, per ringraziarlo, tese il suo lunghissimo collo ritrovato fino alla cima di una palma altissima di FrancaVilla, dove nessuno riusciva mai ad arrivare, e con un morso delicato staccò un enorme casco di banane dorate, dolcissime e profumate. Le depositò con cura ai piedi dell'elefante: la merenda era servita, senza nemmeno passare dalla bottega!

EleFranco si sedette felice e si lanciò nella sua contagiosa risata: OH... OH... OH...""",
    },
    {"num": 4,
        "title": '🦷 Dal Dentista e Pino il Topolino 🐭',
        "missione": 'EleFranco va dal dentista degli elefanti per una pulizia alla zanna sinistra che gli dà fastidio. 🪥',
        "incontro": 'Trova Pino il Topolino che cerca di scavare una tana ma il terreno è pieno di sassi duri che gli rompevano le unghie. 🪓',
        "aiuto": 'EleFranco usa la zanna sinistra come piccone per rimuovere i sassi duri. Lo sfregamento continuo contro la terra sabbiosa e le pietre gratta via tutto il tartaro. 🦫',
        "morale": 'La forza va usata per spianare la strada a chi è più piccolo. ⭐',
        "colpo": "Pino entra nella tana e nota che la zanna di EleFranco splende come l'oro. Lo scavo l'ha lucidata alla perfezione, molto meglio dello spazzolino del dentista. ✨",
        "finale_schema": 'Niente dentista, la zanna è sanissima. Risata: OH... OH... OH...',
        "racconto": """C'era una volta un Elefante di nome Franco, che gli amici chiamavano ... EleFranco. Di cognome faceva Franchini.

Abitava nella sua casa a FrancaVilla, un piccolo borgo radioso incorniciato da una fitta foresta tropicale, dove le farfalle volavano ricamando fili di seta colorata nell'aria, i pappagalli chiacchieravano tra le liane e tutto profumava di gelsomino e di estate perenne.

Era un pomeriggio caldissimo e EleFranco sentiva una sensazione ruvida e fastidiosa alla zanna sinistra, come se ci fosse della sabbia o del tartaro incastrato. Passava la lingua su e giù, ma il fastidio non andava via. «Uffa, così non va,» brontolò. «Devo andare dallo studio del dentista degli elefanti a farmi fare una bella pulizia.» Si infilò i suoi stivali giganti, ben spazzolati per la visita, aprì la porta e si mise in marcia a grandi passi. Il terreno della via tropicale vibrava sotto i suoi piedoni: THUMP THUMP THUMP.

Lungo la strada, vicino alla radice di un grande albero secolare, vide una piccola sagoma grigia tutta sudata e ansante. Era Pino il Topolino, con i baffetti tremanti e le minuscole zampe arrossate.

«Che fatica, EleFranco!» squittì Pino, lasciandosi cadere sfinito. «Sto cercando di scavare la mia nuova tana sotterranea prima che arrivi l'inverno, ma il terreno qui è pieno di sassi durissimi! Ho consumato tutte le unghie e non sono riuscito a smuovere nemmeno un ciottolo. Se non trovo un riparo presto, gelerò di freddo!»

«Non preoccuparti, Pino, una bella casetta calda te la meriti proprio,» disse EleFranco con un sorriso gentile.

Ma poi gettò un'occhiata in direzione dello studio del dottore e la mente cominciò a vagare: si mise a pensare a quante poltrone grandi ci fossero nella sala d'attesa, a che sapore avesse il collutorio alla menta del dottore e se gli avrebbero regalato un adesivo per i bravi pazienti.

Si stava perdendo nei suoi pensieri, ma vedendo lo sguardo disperato del topolino, scosse le grandi orecchie e gridò: "FOCUS!"

«Fatti da parte, piccoletto, alla terra dura ci penso io,» disse rimboccandosi le maniche immaginarie.

Si inclinò di lato con cautela e puntò la sua robusta zanna sinistra contro il terreno sassoso, usandola come un possente piccone. Affondò, fece leva, sollevò e ribaltò: zolle e ciottoli volavano via uno dopo l'altro, mentre dalla roccia schizzavano scintille e nuvolette di polvere.

«Sei una ruspa, EleFranco!» squittiva Pino saltellando di gioia. «Più giù, più giù, lì voglio la camera da letto!» L'elefante scavò con un'energia pazzesca, e lo sfregamento continuo della zanna contro la sabbia abrasiva e le pietre generò un gran calore. In poco tempo la tana fu pronta: ampia, profonda e accogliente, con tanto di corridoio e angolino per le provviste.

EleFranco si rialzò temendo di essersi rovinato la zanna con tutto quel raschiare. «Oh no, l'avrò tutta scheggiata...» mormorò preoccupato. Ma Pino gli corse incontro gridando: «Guardati nel fiume, presto!» L'elefante si specchiò nell'acqua e rimase a bocca aperta: lo scavo vigoroso aveva grattato via ogni traccia di tartaro, lucidando la zanna sinistra fino a farla risplendere come oro massiccio! Era pulitissima e luccicante, molto meglio di come l'avrebbe lasciata lo spazzolino del dentista.

La missione era compiuta e dal dentista non c'era più bisogno di andare!

EleFranco alzò la proboscide e fece ridere tutti con la sua famosa risata: OH... OH... OH...""",
    },
    {"num": 5,
        "title": '🪡 Dal Sarto e Ciccio il Riccio 🦔',
        "missione": 'EleFranco va dal sarto a rammendare la sua giacca preferita che si è strappata su una manica. 🦺',
        "incontro": "Sente gridare aiuto: c'era Ciccio il Riccio, rimasto incastrato in un cespuglio di rovi con tutti i suoi aculei aggrovigliati. 🌿",
        "aiuto": 'EleFranco stende la sua vecchia giacca sopra i rovi per fare da scudo e liberare Ciccio. Nel farlo, però, le spine distruggono completamente la giacca riducendola in stracci. 💥',
        "morale": 'I vecchi oggetti si possono sacrificare, la sicurezza di un amico no. ❤',
        "colpo": 'Ciccio raccoglie i pezzi di stoffa e usando i suoi aculei come aghi cuce una mantella stile "patchwork" coloratissima e super alla moda per EleFranco. 🎨',
        "finale_schema": 'Un nuovo vestito da supereroe totalmente gratis! Risata: OH... OH... OH...',
        "racconto": """C'era una volta un Elefante di nome Franco, che gli amici chiamavano ... EleFranco. Di cognome faceva Franchini.

Abitava nella sua accogliente casa a FrancaVilla, un villaggio pittoresco dove le strade erano lastricate di ciottoli bianchi e le botteghe degli artigiani si susseguivano una dopo l'altra come scatole di giocattoli colorate: il fabbro, il vasaio, il candelaio e, naturalmente, il sarto.

Un mattino, mentre si vestiva, EleFranco notò un brutto strappo sulla manica della sua giacca di velluto preferita. «Oh no, la mia giacca della domenica!» si rammaricò, infilando la zampa nel buco. «Devo andare subito dal sarto del paesino a farla rammendare, prima che lo strappo diventi più grande.» Si infilò le sue scarpe giganti con la suola di gomma, prese la giacca sotto il braccio e uscì di casa. I suoi passi risuonavano pesanti sui ciottoli bianchi: THUMP THUMP THUMP.

Mentre passava vicino a una siepe selvatica, udì dei piccoli lamenti acuti e disperati. Si avvicinò e scostò una foglia: là, in mezzo a un cespuglio di rovi pieni di spine, c'era Ciccio il Riccio, una palletta di aculei marroni completamente aggrovigliata tra i rami spinosi.

«Aiutooo, EleFranco!» squittì Ciccio agitandosi. «Inseguivo una mela caduta e sono finito dritto in questo roveto! Più mi muovo, più i miei aculei si impigliano nelle spine. Sono bloccato da ore e ho una paura tremenda di restare incastrato qui per sempre!»

«Sta' fermo un attimo, Ciccio, non agitarti che peggiori le cose,» disse EleFranco con voce rassicurante.

Ma poi il suo sguardo cadde sulla giacca strappata che teneva sotto il braccio, e la mente prese a vagare: cominciò a pensare a quali fili colorati avrebbe usato il sarto, se avrebbe aggiunto dei bottoni nuovi e luccicanti e magari una toppa elegante sul gomito.

Si stava perdendo in questi pensieri, ma vedendo Ciccio soffrire tra le spine, scosse le orecchie e gridò: "FOCUS!"

«Tieni duro, piccolo, ti tiro fuori io da lì,» promise.

Guardò i rovi acuminati e capì che non poteva afferrare Ciccio con la proboscide senza pungersi. Allora ebbe un'idea: prese la sua amata giacca di velluto e la stese con cura sopra il cespuglio spinoso, creando una morbida passerella protettiva sopra le spine. «Ora cammina sopra la stoffa, Ciccio, piano piano!» Il riccio, passo dopo passo, scivolò fuori dal roveto sano e salvo, senza più un solo aculeo impigliato.

«Ce l'ho fatta! Sono libero!» esultò Ciccio rotolando sull'erba. Ma quando EleFranco recuperò la giacca, il suo sorriso svanì: il velluto era stato ridotto in mille stracci dalle spine, completamente irrecuperabile. «Oh no, la mia giacca preferita... ora è solo un mucchio di brandelli,» sospirò.

Ciccio, però, non si perse d'animo. Raccolse tutti i pezzi di stoffa colorata e, usando i suoi aculei appuntiti come perfetti aghi da cucito, cominciò a lavorare velocissimo: punto dopo punto, cucì insieme i brandelli creando una splendida mantella stile "patchwork", coloratissima e calda. «Provala, EleFranco!» La drappeggiò sulle spalle dell'elefante, che si specchiò in una pozzanghera sentendosi un vero supereroe di FrancaVilla.

La missione era compiuta: altro che rammendo, ora aveva un mantello tutto nuovo!

EleFranco si indossò fiero la mantella e tutta FrancaVilla sentì la famosa risata: OH... OH... OH...""",
    },
    {"num": 6,
        "title": '📚 In Libreria e la Lucciola Luce 🪰',
        "missione": 'EleFranco va in libreria a comprare un nuovo libro di favole da leggere prima di dormire. 🌙',
        "incontro": 'Mentre scende la sera incontra Luce la Lucciola, triste perché ha la febbre e la sua luce si è spenta, impedendole di ritrovare la strada di casa. 🪔',
        "aiuto": 'La fa sedere sulla testa e la accompagna. Per non farle avere paura del buio, EleFranco inizia a inventare e raccontare storie bellissime lungo il cammino. 🌌',
        "morale": 'Quando aiuti qualcuno a trovare la strada, non ti senti mai perso. 🗺',
        "colpo": 'A casa di Luce, centinaia di lucciole volano intorno a EleFranco proiettando sulle rocce le ombre delle storie appena inventate, creando un magico libro animato nel cielo. ✨',
        "finale_schema": 'La favola della buonanotte è già nella sua testa! Risata: OH... OH... OH...',
        "racconto": """C'era una volta un Elefante di nome Franco, che gli amici chiamavano ... EleFranco. Di cognome faceva Franchini!

Abitava nella sua casa a FrancaVilla, un paesino misterioso e affascinante che di notte si illuminava soltanto grazie ai riflessi d'argento del fiume e alle lanterne di carta appese ai balconi, ondeggianti come tante piccole lune addomesticate.

Quella sera, mentre il cielo si tingeva di viola, EleFranco aveva un desiderio: «Mi manca proprio una bella favola nuova per la buonanotte. Andrò alla libreria di FrancaVilla prima che chiuda!» Si infilò le sue ciabatte giganti di lana morbida, perfette per la sera, e uscì di casa. I suoi passi facevano tremare dolcemente le foglie cadute lungo il sentiero: THUMP THUMP THUMP.

Nel boschetto vicino alle case sentì un pianto sottile sottile. Si chinò e, in mezzo al buio, scorse una minuscola creatura dal corpicino tondo, le ali velate e un guscio che avrebbe dovuto brillare ma era spento e grigio. Era Luce la Lucciola, e tremava tutta.

«Oh, EleFranco,» tirò su col naso Luce. «Mi sono presa una brutta febbre e la mia lucina si è spenta del tutto. Senza la mia luce non riesco a ritrovare la strada di casa, e qui nel bosco è tutto così buio e pauroso! Le altre lucciole sono troppo lontane per vedermi.»

«Vieni qui, piccolina, non ti lascio certo da sola al buio,» disse EleFranco con tenerezza.

Ma poi alzò gli occhi alle prime stelle e la mente prese a vagare: cominciò a pensare a quante pagine avesse il libro che voleva comprare, se ci fossero disegni di draghi sputafuoco o di navi pirata, e che colore avrebbe avuto la copertina.

Si stava distraendo, ma sentendo Luce starnutire forte nel buio, scosse le grandi orecchie e gridò: "FOCUS!"

«Niente paura, Luce, ti riporto a casa io, e ti tengo compagnia per tutta la strada,» le promise.

Con delicatezza fece salire la piccola lucciola sulla sua grande testa, vicino al ciuffetto, perché stesse al sicuro e al calduccio. Poi si incamminò nel bosco e, per non farle sentire la paura del buio, cominciò a inventare ad alta voce storie meravigliose: «C'era una volta un gigante buono che teneva le stelle in tasca... e una stella cadente che voleva diventare lampione...» La sua voce profonda riempiva il silenzio, e Luce, ascoltando rapita, dimenticava la febbre e la paura.

Camminando e raccontando, arrivarono finalmente al grande albero delle lucciole. E lì successe la magia: tutta la famiglia di Luce, felice di rivederla, si alzò in volo e cominciò a danzare in cerchio intorno a EleFranco. Centinaia di lucine dorate proiettavano sulle rocce le ombre animate dei racconti dell'elefante: il gigante buono, la stella cadente, le navi e i draghi prendevano vita sulla pietra, creando un magico libro illustrato vivente sospeso nella notte.

EleFranco guardò quello spettacolo a bocca aperta: la favola della buonanotte ce l'aveva già nella testa, e non serviva comprare proprio nulla!

Felice, l'elefante tornò a casa e inondò tutti con la sua famosa risata: OH... OH... OH...""",
    },
    {"num": 7,
        "title": '🚲 Dal Meccanico e Ralph la Talpa \U0001f6de',
        "missione": 'EleFranco va dal meccanico a gonfiare le ruote della sua bicicletta gigante che sono piatte. \U0001f6de',
        "incontro": "Trova Ralph la Talpa che tossisce: ha bucato una galleria sotterranea dove bruciano foglie secche e c'è troppo fumo. 💨",
        "aiuto": 'EleFranco si posiziona sul buco e soffia con tutta la forza dei suoi polmoni per liberare il tunnel. Il super soffio crea un contraccolpo pazzesco che fa sobbalzare la bici. 💥',
        "morale": "Un piccolo gesto d'altruismo può dare una grande spinta. 🚀",
        "colpo": "Il soffio d'aria pulita, rimbalzando nel tunnel, si incanala perfettamente nelle valvole delle ruote della bicicletta, gonfiandole al massimo. 🌬",
        "finale_schema": 'Ruote gonfiate senza meccanico e talpa salva! Risata: OH... OH... OH...',
        "racconto": """C'era una volta un Elefante di nome Franco, che gli amici chiamavano ... EleFranco. Di cognome faceva Franchini.

Abitava a FrancaVilla, un villaggio industrioso tutto mattoni rossi e canali artificiali, dove gli artigiani amavano riparare ingranaggi nelle loro officine fumanti e il ticchettio degli orologi pubblici scandiva allegramente il tempo della comunità.

Quel mattino EleFranco voleva fare un giro in bicicletta, ma scoprì con disappunto che le ruote della sua bici gigante erano completamente a terra, mosce come due frittelle. «Uffa, sono sgonfie sgonfie,» constatò dandoci un colpetto. «Devo spingere la bici fino all'officina del meccanico in paese e farle gonfiare per bene.» Si infilò i suoi robusti stivali giganti da lavoro e si incamminò spingendo il pesante telaio. Sotto quello sforzo, i suoi passi erano ancora più decisi del solito: THUMP THUMP THUMP.

Arrivato vicino a una collinetta erbosa, notò un sottile filo di fumo grigio che usciva da un buco nel terreno, accompagnato da una tosse insistente. Si chinò e vide due piccole zampe a forma di pala e un musetto rosa che spuntava dalla terra: era Ralph la Talpa, con gli occhietti lacrimosi e tossicchiante.

«Cof cof... EleFranco, che guaio!» tossì Ralph. «Stavo scavando una nuova galleria e ho intercettato per sbaglio un vecchio deposito di foglie secche che sta bruciando piano piano sottoterra. Tutto il mio tunnel si è riempito di fumo e io non riesco più a respirare là dentro! Cof cof!»

«Vieni fuori a prendere aria, Ralph, ci penso io a ripulire la tua galleria,» disse EleFranco premuroso.

Ma poi gettò uno sguardo alle ruote sgonfie della bici e la mente cominciò a vagare: si mise a pensare a quanti bar di pressione servissero per gonfiarle al punto giusto, se il meccanico avesse una pompa elettrica nuova fiammante e quanto sarebbe costata la riparazione.

Si stava distraendo, ma un altro accesso di tosse di Ralph lo riportò bruscamente alla realtà.

Scosse le orecchie e gridò: "FOCUS!"

«Tieni duro, amico mio, adesso ti faccio respirare aria pulita,» lo rassicurò.

Si posizionò proprio sopra il foro d'aerazione della galleria, prese il fiato più profondo della sua vita gonfiando il petto come una mongolfiera, e soffiò con tutta la forza dei suoi enormi polmoni dentro il tunnel. Una folata gigantesca spazzò via il fumo da tutti i cunicoli, soffocò le braci e fece uscire dall'altra estremità una nuvola grigia che si dissolse nel cielo. La galleria di Ralph era di nuovo pulita e respirabile.

Ma il super soffio ebbe un effetto a sorpresa: l'aria compressa, rimbalzando freneticamente da una parete all'altra del tunnel, trovò un piccolo soffione naturale che sbucava dal terreno proprio sotto le valvole aperte della bicicletta. In un solo secondo — pffffff! — le due ruote si gonfiarono al massimo, diventando dure e perfette come palloni nuovi!

«Ce l'abbiamo fatta tutti e due!» tossicchiò Ralph, ormai sorridente, mentre EleFranco fissava incredulo le sue gomme. La galleria era salva e le ruote gonfie senza nemmeno arrivare dal meccanico.

EleFranco partì felice sulla sua bici, esordendo con la sua famosa risata: OH... OH... OH...""",
    },
    {"num": 8,
        "title": '🧼 Al Lavaggio Elefanti e Mino il Maialino 🐷',
        "missione": 'EleFranco va al lavaggio per elefanti a farsi una bella doccia profumata perché è pieno di polvere. 🚿',
        "incontro": 'Trova Mino il Maialino, triste perché il sole ha seccato la sua pozzanghera e rischia di scottarsi la pelle. 🤎',
        "aiuto": "EleFranco prende l'acqua dal fiume con la proboscide e bagna la terra ricreando il fango. Il maialino felice si rotola e fa un mega spruzzo che infanga completamente EleFranco. 🟤",
        "morale": 'La felicità degli altri a volte è disordinata, ma ne vale la pena. 🤪',
        "colpo": "All'improvviso scoppia un acquazzone estivo bellissimo che fa una doccia perfetta a EleFranco lasciandolo pulito e profumato, mentre riempie la pozzanghera del maialino. 🌧",
        "finale_schema": 'Lavaggio naturale completato! Risata: OH... OH... OH...',
        "racconto": """C'era una volta un Elefante di nome Franco, che gli amici chiamavano ... EleFranco. Di cognome faceva Franchini.

Abitava nella sua casa a FrancaVilla, un paesino rurale adagiato in una piana di canneti e campi di girasole, dove i trattori colorati raccoglievano il grano dorato, i canali d'acqua disegnavano linee geometriche perfette sulla terra e l'aria sapeva di fieno appena tagliato.

Dopo una mattinata di lavori in giardino, EleFranco era tutto coperto di una polvere grigia che gli faceva prudere la pelle. «Brrr, che sporcizia, sembro una statua impolverata,» disse guardandosi le zampe. «Ho proprio bisogno di andare al Lavaggio Elefanti del paesino a farmi una bella doccia al profumo di fragola.» Si infilò i suoi stivali giganti di gomma azzurra ed uscì di casa. Ad ogni passo gli stivali producevano un suono sordo e gommoso sulla strada: THUMP THUMP THUMP.

Passando vicino alla fattoria, sentì un mugolio sconsolato provenire da una conca di terra secca. Si avvicinò e vide Mino il Maialino, rosa e paffuto, con il codino a ricciolo tutto floscio, che si guardava intorno disperato sotto il sole cocente.

«Oink, EleFranco, che disastro!» mugolò Mino. «Il sole ha prosciugato tutta la mia pozzanghera di fango, e senza non posso rinfrescarmi! La mia pelle è delicatissima e se resto sotto questo solleone rischio di scottarmi tutta. Ho già il musetto che brucia!»

«Tranquillo, Mino, una bella pozza fresca te la rimetto in piedi in un attimo,» disse EleFranco con un sorriso.

Ma poi pensò alla doccia profumata che lo aspettava e la mente prese a vagare: cominciò a immaginare quanti getti d'acqua avesse il lavaggio automatico, se le grandi spazzole rotanti gli avrebbero fatto il solletico sulla pancia e che profumo avesse il sapone, se di fragola o di mela.

Si stava distraendo, ma un piccolo lamento di Mino lo riportò di colpo alla realtà.

Scosse le grandi orecchie e gridò: "FOCUS!"

«Niente paura, amico, ti preparo subito il fango più bello di tutta la fattoria,» promise.

Corse al canale vicino, riempì la proboscide d'acqua fresca e tornò a spruzzarla con cura sulla terra secca della conca, mescolando poi il terreno con la punta del nasone finché non ottenne un fango morbido, fresco e perfetto. «Ecco fatto, salta dentro!» Mino non se lo fece dire due volte: si tuffò nella pozza con un gridolino di gioia e cominciò a rotolarsi felice. Ma rotolando fece uno spruzzo gigantesco di fango che investì EleFranco in pieno, dalla testa alla coda, infangandolo tutto da capo!

«Ops...» fece l'elefante, ora più sporco di prima, con il fango che gli colava perfino dalle orecchie. «Adesso al lavaggio dovrò proprio andarci due volte!»

Ma proprio in quel momento, dal cielo limpido, scoppiò all'improvviso un bellissimo acquazzone estivo, tiepido e scrosciante. Le gocce lavarono EleFranco da ogni traccia di fango e polvere, lasciandolo pulito, lucido e profumato come appena uscito dalla doccia, mentre riempivano fino all'orlo la pozzanghera di Mino, che sguazzava raggiante.

La missione era compiuta, e gratis, grazie alla natura!

EleFranco alzò la proboscide e fece sorridere tutti con la sua famosa risata: OH... OH... OH...""",
    },
    {"num": 9,
        "title": '🥾 Dal Calzolaio e Bruno il Bruco 🐛',
        "missione": "EleFranco va dal calzolaio a ritirare i suoi enormi stivali invernali per l'anno prossimo. 👢",
        "incontro": 'Sulla strada incontra Bruno il Bruco che piange disperato: deve andare a un ballo ma ha ben 42 scarpine con i lacci tutti aggrovigliati tra loro. 🥾',
        "aiuto": 'EleFranco, usando la punta sensibile della proboscide con millimetrica pazienza, scioglie tutti i nodi uno a uno. Ma la concentrazione è così tanta che gli viene un forte crampo alla proboscide che si arrotola come una molla. 🌀',
        "morale": 'La pazienza scioglie anche i nodi più difficili della via.',
        "colpo": 'Per ringraziarlo, il bruco e i suoi amici fanno un massaggio ritmico a passo di danza sulla proboscide di EleFranco. I loro piccoli colpetti curano il crampo e rilassano i suoi piedi, come se indossasse già i migliori stivali del mondo. \U0001faa9',
        "finale_schema": 'I piedi stanno benissimo senza scarpe nuove! Risata: OH... OH... OH...',
        "racconto": """C'era una volta un Elefante di nome Franco, che gli amici chiamavano ... EleFranco. Di cognome faceva Franchini.

Abitava a FrancaVilla, un paesino montano circondato da cime innevate e boschi di pini secolari, dove le case avevano grandi tetti spioventi di legno scuro, i camini odoravano costantemente di castagne arrostite e l'aria frizzante pizzicava il naso.

Quella mattina EleFranco aveva un impegno: «Devo andare dal calzolaio a ritirare i miei stivali invernali giganti, quelli foderati di pelliccia. L'inverno è alle porte!» Si infilò i suoi stivali leggeri da mezza stagione ed uscì di casa. Il rumore dei suoi passi cadenzava la marcia sul selciato di montagna: THUMP THUMP THUMP.

Lungo la via, seduto su una grande foglia accartocciata, c'era una piccola creatura verde e pelosetta che singhiozzava sconsolata. Era Bruno il Bruco, lungo e morbido, con tante minuscole zampette e un musetto tristissimo.

«Che catastrofe, EleFranco!» piagnucolò Bruno. «Stasera c'è il grande Ballo della Primavera di FrancaVilla e io non posso andarci! Ho ben quarantadue scarpine, una per ogni zampetta, e mi si sono aggrovigliati tutti i lacci in un unico, enorme, impossibile nodo! Più tiro, più si stringe. Non riesco nemmeno a muovermi!»

«Quarantadue scarpine? Caspita, che impresa!» sorrise EleFranco. «Ma non ti preoccupare, Bruno, quel nodo lo sbroglieremo insieme.»

Poi però guardò il sentiero che portava dal calzolaio e la mente cominciò a vagare: si mise a pensare a quanto fossero spesse le suole dei suoi nuovi stivali invernali, al profumo del cuoio fresco nella bottega e a quanto sarebbero stati caldi durante le nevicate.

Si stava distraendo, ma un singhiozzo più forte di Bruno lo richiamò all'ordine.

Scosse le orecchie e disse: "FOCUS!"

«Sta' tranquillo, piccolo, con un po' di pazienza ti libero zampetta per zampetta,» lo rassicurò.

Si chinò pian piano sulla foglia e, usando la punta ultra-sensibile della proboscide come fossero due dita delicatissime, cominciò a districare il groviglio. Sciolse un laccio, poi un altro, e un altro ancora, con una pazienza infinita e una precisione millimetrica. «Ecco la numero dieci... la venti... la trenta...» contava EleFranco, mentre Bruno tratteneva il respiro per non muoversi.

Ma quella concentrazione estrema ebbe il suo prezzo: a forza di tenere la proboscide tesa e immobile, all'elefante venne un crampo tremendo, e il nasone gli si arrotolò di scatto su se stesso come una molla d'acciaio! «Ahia ahia ahia!» mugolò EleFranco, con la proboscide tutta attorcigliata e dolorante.

Bruno, ormai libero con tutte e quarantadue le scarpine perfettamente allacciate, non lo lasciò certo soffrire. Chiamò a raccolta i suoi fratelli bruchi e tutti insieme salirono sulla proboscide attorcigliata, mettendosi a fare un allegro massaggio a passo di danza. Tip tap, tip tap, i loro piccoli colpetti ritmici scioglievano il crampo nodo dopo nodo, e quel calpestio leggero rilassò così tanto anche i piedi stanchi dell'elefante che li sentì caldi e morbidi, come se indossasse già le scarpe più comode del mondo.

«Mi sembra di camminare sulle nuvole!» rise EleFranco distendendo finalmente la proboscide. Gli stivali nuovi potevano aspettare: i suoi piedi stavano già benissimo!

EleFranco alzò la proboscide e tutti si girarono a sentire la famosa risata: OH... OH... OH...""",
    },
    {"num": 10,
        "title": '✉ Dal Postino e Renatolo lo Scoiattolo 🐿',
        "missione": "EleFranco va all'ufficio postale a spedire una letterina importante per il suo cuginetto lontano. 📬",
        "incontro": 'Incontra Renatolo lo Scoiattolo sotto una grande quercia. Renatolo ha fatto cadere le sue scorte di ghiande invernali in un buco strettissimo tra le radici e non riesce ad arrivarci. 🪵',
        "aiuto": "EleFranco infila la proboscide nel buco a mo' di cannuccia e aspira le ghiande. Ma ne aspira una di troppo, che gli si incastra nel naso facendolo starnutire continuamente. 👃",
        "morale": 'Condividere il peso altrui rende i legami più forti. 💪',
        "colpo": "Con l'ultimo potentissimo starnuto, EleFranco spara via la ghianda bloccata insieme alla sua letterina cartacea. La lettera vola nel cielo e atterra precisamente dentro il sacco del postino tre vie più in là! 🚀",
        "finale_schema": 'Lettera spedita con posta super-aerea! Risata: OH... OH... OH...',
        "racconto": """C'era una volta un Elefante di nome Franco, che gli amici chiamavano ... EleFranco. Di cognome faceva Franchini.

Abitava nella sua casa a FrancaVilla, un paesino costiero battuto da una dolce brezza marina, dove i vicoli profumavano di salsedine, i gabbiani si rincorrevano nel cielo e le barche da pesca riposavano sul bagnasciuga dorato come grandi gusci colorati.

Quel mattino EleFranco aveva scritto una bellissima lettera, piena di disegni e di saluti affettuosi, per il suo cuginetto che viveva lontano. «Devo correre all'ufficio postale prima che passi il postino di mezzogiorno,» si disse stringendo la busta. Si infilò i suoi stivali giganti rossi, aprì la porta e si diresse verso la piazza. Il terreno risuonava sotto il suo peso massiccio: THUMP THUMP THUMP.

Sotto la grande quercia secolare della piazza, sentì un disperato squittio. Alzò lo sguardo e vide Renatolo lo Scoiattolo, dalla coda folta e ramata, che si torceva le zampette davanti a una fessura tra le radici dell'albero.

«EleFranco, è una tragedia!» squittì Renatolo. «Stavo sistemando le mie provviste per l'inverno quando mi è scivolato tutto il sacchetto, e tutte le mie ghiande sono cadute in questa fessura strettissima e profonda tra le radici! La mia zampa non ci entra e senza quelle scorte non sopravvivrò al freddo. Le sento là sotto e non posso prenderle!»

«Calmati, Renatolo, le tue ghiande le recuperiamo tutte fino all'ultima,» lo rassicurò EleFranco.

Ma poi pensò alla sua lettera e la mente prese a vagare: cominciò a chiedersi quanti francobolli servissero per una spedizione così lontana, che faccia avrebbe fatto il cuginetto aprendo la busta e se la lettera sarebbe arrivata in tempo per la sua Festa.

Si stava distraendo, ma il pianto sconsolato di Renatolo lo scosse.

Allora aprì le grandi orecchie e gridò: "FOCUS!"

«Tieni il cesto pronto, amico, che te le tiro su tutte io,» disse strizzandogli l'occhio.

Infilò la punta della proboscide nella fessura e cominciò a usarla come una potente cannuccia, aspirando le ghiande una a una e sputandole delicatamente nel cesto di Renatolo. «Una, due, tre... quante ne avevi!» rideva l'elefante. Ma a un certo punto aspirò con troppa foga e una ghianda di troppo gli risalì dritta su per la proboscide, andandosi a incastrare proprio in fondo al naso. «Eh? Ehm... ho il naso... ho il naso pieno... ATC- aspetta...» Un solletico pazzesco cominciò a salirgli su per il nasone, irrefrenabile.

EleFranco caricò tutto il fiato che aveva in corpo, gli occhi gli si strinsero, il petto si gonfiò e poi — YAAATCIÙÙÙ! — esplose nello starnuto più potente della storia di FrancaVilla. Il soffio stratosferico sparò via la ghianda incastrata come un proiettile, e insieme a lei volò via anche la lettera che l'elefante teneva nel taschino! La busta si alzò in cielo, planò sopra i tetti, virò con la brezza marina e atterrò con precisione millimetrica dritta dentro il sacco del postino, tre vie più in là, che stava giusto facendo il suo giro.

«Spedita! È spedita!» esultò Renatolo, mentre EleFranco si stropicciava il naso incredulo. Le ghiande erano salve e la lettera in viaggio, il tutto senza nemmeno entrare all'ufficio postale.

EleFranco alzò la proboscide e travolse tutti con la sua famosa risata: OH... OH... OH...""",
    },
    {"num": 11,
        "title": '🏥 In Ospedale per il Controllo e Mietta la Scimmietta 🐒',
        "missione": 'EleFranco va in ospedale a fare il controllo annuale per sentire se il suo cuore batte forte e sano.',
        "incontro": "Incontra Mietta la Scimmietta, terrorizzata perché deve fare un'iniezione e ha tanta paura dei dottori e degli aghi. 💉",
        "aiuto": 'EleFranco la prende in braccio e per distrarla inizia a fare dei giochi buffissimi con le orecchie, sventolandole e imitando i versi di tutti gli animali del bosco. Mietta ride così tanto che non si accorge della puntura. 🩺',
        "morale": 'Il coraggio si trova più facilmente quando si ride insieme. 😂',
        "colpo": 'Il dottore primario usa lo stetoscopio su EleFranco mentre sta ancora ridendo di cuore. Dice: "Il tuo cuore è pieno di gioia ed è sanissimo, non serve fare nessun altro esame!". 🥰',
        "finale_schema": 'Controllo superato a pieni voti grazie alle risate! Risata: OH... OH... OH...',
        "racconto": """C'era una volta un Elefante di nome Franco, che gli amici chiamavano ... EleFranco. Di cognome faceva Franchini.

Abitava nella sua casa a FrancaVilla, un paesino antico caratterizzato da alti campanili di pietra e cortili nascosti, dove le fontane medievali zampillavano acqua fresca, gli anziani sedevano all'ombra dei portici a parlare del tempo e i piccioni passeggiavano impettiti sui sampietrini.

Quel giorno era il momento della sua visita medica annuale. «Devo andare in ospedale a farmi controllare il cuore, così sono sicuro che batta forte e sano,» si disse posandosi una zampa sul petto. Si infilò i suoi stivali giganti da passeggio ed uscì di casa. Ad ogni suo passo pesante, le strade di pietra producevano un suono ritmico: THUMP THUMP THUMP.

Entrato nella grande sala dell'ospedale, sentì delle urla acutissime. Su una sedia, aggrappata con tutte e quattro le zampe alla spalliera, c'era Mietta la Scimmietta, piccola e pelosa, con gli occhioni spalancati dal terrore, mentre un'infermiera le si avvicinava reggendo una siringa luccicante.

«Nooo, non voglio la puntura!» strillava Mietta tremando. «Ho una paura tremenda degli aghi e dei dottori, EleFranco! Mi gira la testa solo a guardarla. Ti prego, portami via da qui, scappiamo!»

«Ehi, ehi, piccola Mietta, non c'è niente da temere,» disse EleFranco avvicinandosi con dolcezza. «Una puntura dura meno di un battito di ciglia.»

Ma poi gettò un'occhiata verso lo studio del primario e la mente cominciò a vagare: si mise a pensare a quanto fosse grande lo stetoscopio del medico, se sarebbe stato freddo sul petto e a quanti battiti al minuto facesse il suo grande cuore di elefante.

Si stava distraendo, ma un urlo disperato di Mietta lo risvegliò.

Scosse le orecchie e si disse: "FOCUS!"

«Vieni qui da me, Mietta, ci penso io a farti passare la paura,» disse aprendo le braccia.

Prese la scimmietta tremante tra le sue zampe robuste e cominciò il suo spettacolo: mosse le enormi orecchie a sventola, facendole svolazzare come due ali buffe, e si mise a imitare i versi di tutti gli animali, ma tutti sbagliati! Faceva il leone con una vocina da papera, il cane con il fischio di un treno, il gatto con il barrito di un elefante. «Bau! No, aspetta... muuu! No no... cip cip ruggitooo!»

Mietta scoppiò a ridere a crepapelle, dimenticandosi completamente di dove si trovasse. Rideva così forte e di gusto che, quando l'infermiera le fece la puntura sul braccino, non sentì assolutamente nulla. «È... è già finita?» chiese stupita, ancora con le lacrime di risata agli occhi.

Proprio in quel momento entrò il dottore primario e, vedendo l'elefante ridere di cuore insieme alla piccola paziente, gli appoggiò lo stetoscopio sul petto per ascoltare. Sorrise: «Sentite che meraviglia: un cuore che ride così è il più sano e felice di tutta FrancaVilla! Visita superata a pieni voti, EleFranco, non serve nessun altro esame.»

La missione era compiuta, e con tante risate in regalo!

EleFranco alzò la proboscide e tutti lo seguirono nella sua famosa risata: OH... OH... OH...""",
    },
    {"num": 12,
        "title": '💡 In Ferramenta per una Lampadina e Tufo il Gufo 🦉',
        "missione": 'EleFranco va in ferramenta a comprare una nuova lampadina per il suo salotto perché quella vecchia si è fulminata. 🔌',
        "incontro": 'Incontra Tufo il Gufo che cerca di dormire, ma un gruppo di uccellini dispettosi sta facendo un baccano tremendo impedendogli di chiudere occhio. 🦜',
        "aiuto": "EleFranco si siede sotto l'albero e allarga le sue enormi orecchie per coprire il ramo di Tufo, facendo da isolamento acustico. Rimanendo al buio immobile, EleFranco si addormenta profondamente pure lui. 👂",
        "morale": 'Proteggere la pace di chi è stanco porta serenità anche a noi stessi. 💤',
        "colpo": 'Quel riposo incredibile fa sì che, quando si sveglia, i suoi occhi brillino di una luce così viva da illuminare la via. Arrivato a casa, si accorge di quanto la casa sia già splendidamente illuminata dalla luce naturale del sole. ☀',
        "finale_schema": 'Chi ha bisogno della lampadina quando si è così radiosi? Risata: OH... OH... OH...',
        "racconto": """C'era una volta un Elefante di nome Franco, che gli amici chiamavano ... EleFranco. Di cognome faceva Franchini.

Abitava nella sua accogliente casa all'interno del paesino di FrancaVilla, una borgata magica coperta da tetti di tegole azzurre, dove i giardini pensili traboccavano di rose bianche e i muri delle case erano dipinti con bellissimi affreschi che raccontavano storie antiche.

Quel pomeriggio la lampadina del suo salotto si era fulminata con un piccolo "tac". «Al buio non ci leggo le favole, così non va,» borbottò EleFranco. «Devo andare subito in ferramenta a comprare una bella lampadina nuova.» Si infilò i suoi stivali giganti da passeggio, aprì la porta e si diresse verso il negozio. Camminava sul marciapiede col suo passo pesante: THUMP THUMP THUMP.

Sotto un grande albero della piazza, sentì un lamento stanco e vide due grandi occhi gialli cerchiati da occhiaie scurissime. Era Tufo il Gufo, appollaiato su un ramo, con le piume arruffate e l'aria sfinita di chi non dorme da giorni.

«Uffa, EleFranco, sono distrutto,» sbadigliò Tufo. «Io sono un uccello notturno e dovrei dormire di giorno, ma un gruppo di uccellini dispettosi si è messo a cinguettare e fare baccano proprio sul mio albero! Non riesco a chiudere occhio da tre giorni e ho un sonno arretrato che non ti dico. Le piume mi tremano dalla stanchezza.»

«Povero Tufo, un bel sonnellino te lo meriti proprio,» disse EleFranco con comprensione.

Ma poi pensò alla lampadina e la mente prese a vagare: cominciò a chiedersi quanti watt servissero per illuminare bene il salotto, se la lampadina nuova sarebbe stata a forma di pera o di goccia e quanto fosse difficile montarla sul soffitto così alto.

Si stava perdendo in questi pensieri, ma vedendo le ali di Tufo tremare per la stanchezza, si concentrò, scosse le orecchie e gridò: "FOCUS!"

«Riposa tranquillo, amico mio, al silenzio ci penso io,» sussurrò per non disturbare.

Si sedette con delicatezza ai piedi del tronco e allargò le sue enormi orecchie a sventola, avvolgendole tutt'intorno al ramo di Tufo come due grandi tende insonorizzate. Di colpo il cinguettio chiassoso degli uccellini si trasformò in un ovattato e lontano sussurro. Tufo sospirò di sollievo, chiuse i grandi occhi gialli e in pochi istanti si addormentò beato.

Ma stando lì fermo, al caldo e al buio creato dalle proprie orecchie, anche EleFranco fu cullato dal silenzio e — senza accorgersene — si addormentò profondamente pure lui, per ben due ore, con un dolce russare. Quando finalmente si svegliò, riposato come non mai, sentì gli occhi stranamente vivi e luminosi: quel sonno rigenerante li aveva fatti brillare di una luce così intensa da rischiarare la via davanti a lui.

Arrivato a casa, aprì la porta e scoppiò a ridere: il sole del tardo pomeriggio entrava dalle finestre e illuminava il salotto alla perfezione, caldo e dorato. «Ma allora di lampadine non ho proprio bisogno!» esclamò felice.

La missione era compiuta grazie all'altruismo (e a un bel pisolino)!

EleFranco inserì la proboscide all'insù e rallegrò tutti con la sua famosa risata: OH... OH... OH...""",
    },
    {"num": 13,
        "title": "🍪 In Pasticceria per i Biscotti e Fosco l'Orso 🐻",
        "missione": 'EleFranco va in pasticceria a comprare i biscotti allo zenzero che gli piacciono tanto. 🍩',
        "incontro": "Trova Fosco l'Orso incastrato con la testa dentro un alveare vuoto nel tentativo di leccare gli ultimi rimasugli di miele. 🐝",
        "aiuto": "EleFranco tira l'alveare con la proboscide per liberarlo. Quando la testa dell'orso esce fuori... l'alveare rimbalza all'indietro spiaccicandosi sulla testa di EleFranco, coprendolo di miele appiccicoso. 🍯",
        "morale": 'La dolcezza condivisa raddoppia sempre il suo valore. ❤',
        "colpo": "Dal cielo cade una pioggia di polline dorato dai fiori che si attacca al miele sulla sua testa. L'unione di miele e polline si asciuga al sole creando dei biscotti croccanti e dolcissimi proprio sul suo ciuffo! 🌾",
        "finale_schema": 'Biscotti fatti in casa direttamente sulla testa! Risata: OH... OH... OH...',
        "racconto": """C'era una volta un Elefante di nome Franco, che gli amici chiamavano ... EleFranco. Di cognome faceva Franchini.

Abitava nella sua accogliente casa a FrancaVilla, un paesino nordico incastonato in una vallata di abeti rossi e laghi ghiacciati, dove l'aria frizzante pungeva le guance, il fumo dei comignoli saliva dritto nel cielo terso e le case avevano caldi pavimenti di pietra riscaldati dal fuoco.

Quel pomeriggio EleFranco aveva una gran voglia di qualcosa di dolce. «Mmm, mi vedo proprio un bel sacchetto di biscotti allo zenzero, croccanti e profumati,» fantasticò leccandosi la proboscide. «Vado subito alla pasticceria prima che sfornino l'ultima teglia.» Si infilò i suoi stivali giganti di cuoio morbido ed uscì di casa. I suoi passi risuonavano sulla via innevata: THUMP THUMP THUMP.

Vicino a un grande albero cavo, sentì dei versi strozzati e un gran dimenarsi. Si avvicinò e vide una scena buffissima e preoccupante insieme: Fosco l'Orso, grande e bruno, era in piedi sulle zampe posteriori con la testa completamente infilata e incastrata dentro un grosso alveare di legno appeso a un ramo, e agitava le zampe nel vuoto.

«Mmmf! Mmmpf! EleFranco, aiuto!» arrivò la voce ovattata di Fosco da dentro l'arnia. «Volevo solo leccare gli ultimi rimasugli di miele rimasti sul fondo, ma ho infilato la testa troppo a fondo e ora sono incastrato! Non riesco più a tirarla fuori e qui dentro è tutto buio e appiccicoso!»

«Sta' fermo, Fosco, non tirare che peggiori le cose,» raccomandò EleFranco. «Adesso ti libero io.»

Ma poi pensò ai biscotti e la mente cominciò a vagare: si mise a immaginare quanti biscotti ci fossero nel sacchetto della pasticceria, se fossero a forma di omino con i bottoni di zucchero e se la commessa gliene avrebbe regalato uno in più, ancora caldo.

Si stava distraendo, ma un lamento soffocato di Fosco lo riportò bruscamente al presente.

Scosse le orecchie e gridò: "FOCUS!"

«Conta fino a tre e resta rigido, Fosco: uno, due... e tre!» lo avvisò.

Afferrò saldamente l'alveare con la proboscide, piantò bene le zampe nella neve e cominciò a tirare con tutta la sua forza. L'arnia non voleva saperne di cedere; EleFranco tirò ancora più forte e poi, con un sonoro SBLOCK!, la testa di Fosco schizzò fuori di colpo. Ma per il contraccolpo l'alveare gli sfuggì di proboscide e gli rimbalzò all'indietro, spiaccicandosi proprio sulla testa dell'elefante e ricoprendogli tutto il ciuffetto di miele dorato e appiccicosissimo!

«Pffff... che pasticcio,» sbuffò EleFranco, con il miele che gli colava lento sulla fronte e Fosco che si leccava il muso, finalmente libero.

Ma proprio in quell'istante un soffio di vento freddo del nord sollevò dai fiori invernali una pioggia dorata di polline, che si posò leggera sopra il miele appiccicoso del suo ciuffo. Il sole pallido fece il resto: l'impasto di miele e polline si rapprese e si asciugò, trasformandosi in tanti biscotti croccanti, dorati e dolcissimi, proprio lì, sulla testa dell'elefante!

«Ma sono... biscotti veri!» esclamò Fosco assaggiandone uno. Erano deliziosi. La missione era compiuta gratis, e i due amici si sedettero a sgranocchiarli felici sulla neve.

EleFranco alzò la proboscide e partì con la sua famosa risata: OH... OH... OH...""",
    },
    {"num": 14,
        "title": '🪴 Dal Vivaio per i Fiori e Lalla la Farfalla 🦋',
        "missione": 'EleFranco va al vivaio a comprare dei semi di margherite da piantare nel suo giardino. 🌸',
        "incontro": "Incontra Lalla la Farfalla con l'ala bagnata da una goccia di rugiada gigante; non riesce a volare per scappare da un gatto curioso.",
        "aiuto": "EleFranco usa le sue grandi orecchie come ventagli per creare una brezza calda e asciugare l'ala di Lalla. Lo sventolio continuo sposta un cumulo di foglie secche che copre interamente EleFranco. 🌬",
        "morale": 'Un piccolo soffio di gentilezza può salvare una vita intera. 🍃',
        "colpo": "Sotto le foglie c'erano migliaia di semi selvatici di papaveri e margherite che si impigliano nei peli delle zampe di EleFranco. Camminando verso casa, EleFranco semina tutto il sentiero senza accorgersene! 🗺",
        "finale_schema": 'Il giardino e la strada sono già fioriti da soli! Risata: OH... OH... OH...',
        "racconto": """C'era una volta un Elefante di nome Franco, che gli amici chiamavano ... EleFranco. Di cognome faceva Franchini.

Abitava nella sua casa a FrancaVilla, un borgo fiorito sospeso su colline di ulivi argentati e vigne secolari, dove le case avevano facciate color pastello, le persiane scricchiolavano dolcemente al vento e l'aria profumava di terra bagnata e di mosto.

Quel mattino EleFranco voleva abbellire il suo prato un po' spoglio. «Ci vorrebbe un bel tappeto di margherite colorate,» pensò guardando il giardino. «Vado al vivaio a comprare un sacchetto di semini.» Si infilò i suoi stivali giganti ed uscì di casa. I suoi passi scandivano allegri il tempo lungo il sentiero: THUMP THUMP THUMP.

Vicino a un cespuglio, sentì un disperato battito d'ali e un gridolino sottile. Si chinò e scorse Lalla la Farfalla, dalle ali di velluto azzurro e arancio, una delle quali era appesantita e incollata da un'enorme goccia di rugiada. Lì accanto, acquattato nell'erba, un gatto curioso si avvicinava quatto quatto con gli occhi fissi su di lei.

«Aiuto, EleFranco!» squittì Lalla agitando l'ala libera. «Una goccia di rugiada gigante mi ha inzuppato l'ala e non riesco più a volare! E quel gatto si sta avvicinando sempre di più... se non mi asciugo in fretta non riuscirò a scappare. Ho tanta paura!»

«Stai tranquilla, Lalla, quel gatto non ti torcerà nemmeno un'antenna,» la rassicurò EleFranco mettendosi tra lei e il felino.

Ma poi pensò ai suoi fiori e la mente prese a vagare: cominciò a immaginare quante margherite sarebbero spuntate nel suo giardino, di che colore, e quanta acqua avrebbe dovuto usare ogni mattina per annaffiarle.

Si stava distraendo, ma il miagolio impaziente del gatto lo ridestò.

Scosse le grandi orecchie e disse: "FOCUS!"

«Eccomi, piccola, ora ti asciugo io quell'ala in un battibaleno,» le disse con dolcezza.

Si posizionò davanti alla farfalla e cominciò a muovere lentamente le sue enormi orecchie come fossero due grandi ventagli, creando una brezza tiepida e costante. La gocciolina sull'ala di Lalla si rimpicciolì, poi evaporò del tutto, e la farfalla, leggera come prima, spiccò il volo felice ben lontano dal gatto deluso. «Grazie, EleFranco! Mi hai salvato la vita!» cinguettò volteggiando.

Ma quel vigoroso sventolio aveva sollevato dal sentiero un immenso cumulo di foglie secche, che ricaddero tutte addosso all'elefante seppellendolo completamente, fino a far spuntare solo la punta della proboscide. «Bleah, sono una montagna di foglie ambulante,» sbuffò EleFranco scrollandosi mentre si rimetteva in cammino verso casa, stanco.

Quello che non sapeva era che, nascosti sotto quelle foglie secche, c'erano migliaia di semini selvatici di papaveri e margherite, e si erano tutti impigliati nei peli ruvidi delle sue zampe. Così, passo dopo passo, lungo tutto il tragitto verso casa, EleFranco seminò senza accorgersene l'intero sentiero. E poche settimane dopo, come per magia, tutta la stradina fiorì da sola in un'esplosione meravigliosa di rosso e di bianco, più bella di qualsiasi giardino comprato al vivaio!

EleFranco guardò lo spettacolo e scoppiò nella sua famosa risata: OH... OH... OH...""",
    },
    {"num": 15,
        "title": '🍦 In Gelateria e Mayer la Cagnolina 🐶',
        "missione": 'EleFranco va in gelateria a prendere un cono gigante al gusto pistacchio e crema. 🍧',
        "incontro": 'Trova Mayer la Cagnolina, un meticcio dorato tanto dolce da salvataggio che ha perso la sua borraccia termica in cima a una collinetta di sassi e muore di caldo. 🪨',
        "aiuto": "Recupera la borraccia e usa la sua proboscide per aspirare aria fredda dall'ombra del bosco e soffiarla addosso a Mayer. Lo sbalzo termico fa venire a EleFranco un super brivido freddo alla schiena! ❄",
        "morale": "Rinfrescare il cuore di un amico scalda l'anima. 🤍",
        "colpo": "Mayer apre la sua borraccia speciale: dentro c'era del latte di cocco ghiacciato e frutti di bosco che, versato sulla proboscide ancora fredda di EleFranco, si solidifica in un gelato artigianale squisito. 🍼",
        "finale_schema": 'Gelato al volo più buono di quello della gelateria! Risata: OH... OH... OH...',
        "racconto": """C'era una volta un Elefante di nome Franco, che gli amici chiamavano ... EleFranco. Di cognome faceva Franchini.

Abitava a FrancaVilla, un paesino vulcanico sorto vicino a sorgenti termali fumanti, dove il terreno emanava dolci vapori benefici, le rocce scure di lava creavano uno splendido contrasto con l'acqua turchese dei laghetti e l'aria sapeva di zolfo e di fiori di montagna.

Era una giornata caldissima e a EleFranco venne una voglia irresistibile di qualcosa di fresco. «Un bel cono gigante al pistacchio e crema, ecco cosa ci vuole con questo caldo!» esclamò leccandosi già le labbra. Si infilò i suoi stivali giganti estivi ed uscì di casa. Il terreno tiepido risuonava sotto i suoi piedoni: THUMP THUMP THUMP.

Presso una collinetta di sassi arroventati dal sole, sentì un ansito affannoso. Si avvicinò e vide Mayer la Cagnolina, un dolce meticcio dal pelo dorato, una di quelle cagnoline da salvataggio sempre pronte ad aiutare. Quel giorno, però, era lei ad aver bisogno: ansimava sfinita con la lingua di fuori, accasciata all'ombra di un masso.

«Aiuto, EleFranco,» mugolò Mayer con un filo di voce. «Fa un caldo insopportabile e ho una sete tremenda, ma la mia borraccia dell'acqua è rotolata fin lassù, in cima a quella pila di sassi instabili, e io sono troppo stanca e accaldata per arrampicarmi a riprenderla. Sto per svenire dal caldo!»

«Resisti, Mayer, alla tua borraccia ci penso io,» disse subito EleFranco con tono deciso.

Ma poi pensò alla gelateria della piazza e la mente prese a vagare: cominciò a chiedersi quante palline avrebbe preso, se aggiungere la panna montata, una cialda croccante e magari una spruzzata di granella.

Si stava perdendo in queste dolci fantasie, ma vedendo Mayer ansimare sempre più affannosamente, scosse le orecchie e gridò: "FOCUS!"

«Eccomi, amica, ora ti rinfresco io in un attimo,» le promise.

Allungò la proboscide su per i sassi e recuperò con delicatezza la borraccia, riportandola a Mayer che bevve avidamente. Poi ebbe un'idea geniale: infilò il nasone nell'ombra fresca del bosco vicino, aspirò un lungo flusso d'aria gelida e tornò a soffiarla dolcemente sul muso e sul pelo di Mayer, ventilandola come un grande condizionatore naturale. «Aaah, che sollievo,» sospirò la cagnolina riprendendosi a vista d'occhio.

Ma quello sbalzo di temperatura giocò un brutto scherzo all'elefante: un brivido freddo gli corse lungo tutta la schiena e — brrr! — la proboscide gli rimase tutta gelata e rigida, fredda come un ghiacciolo. «Ho il naso congelato!» castagnò EleFranco battendo i denti.

Mayer, ormai ristabilita, volle ringraziarlo a modo suo. Aprì la sua borraccia speciale, che dentro custodiva del latte di cocco ghiacciato mescolato a frutti di bosco, e lo versò sulla proboscide ancora gelata dell'amico. A contatto con quel freddo, il liquido si rapprese all'istante, solidificandosi in un gelato artigianale cremosissimo e squisito, proprio lì, su un bastoncino tenuto dalla proboscide!

«Ma è più buono di quello della gelateria!» esclamò EleFranco assaggiandolo. La missione era compiuta, fresca e dolce, senza nemmeno arrivare in piazza.

EleFranco alzò la proboscide e si lanciò nella sua contagiosa risata: OH... OH... OH...""",
    },
    {"num": 16,
        "title": '📰 In Edicola per il Fumetto e Betta la Scimmietta 🐒',
        "missione": 'EleFranco va in edicola a comprare l\'ultimo numero del fumetto di "Super-Elefante".',
        "incontro": 'Incontra Betta la Scimmietta freddolosa che ha perso la sua sciarpa su un ramo altissimo della giungla e trema tutta. 🧣',
        "aiuto": "Si alza sulle zampe posteriori e con la proboscide afferra la sciarpa lassù. Lo sforzo dell'allungamento fa fare un rumore incredibile alla sua schiena: SCRACK! 💥",
        "morale": 'I veri supereroi non hanno bisogno di un mantello, basta una proboscide tesa. ✨',
        "colpo": "La scimmietta al caldo lancia a EleFranco un vecchio foglio di giornale colorato rimasto sul ramo. È proprio la pagina centrale inedita del fumetto che EleFranco cercava, volata via dall'edicola il giorno prima! 🗞",
        "finale_schema": 'Il fumetto è completo ed EleFranco è il vero Super-Elefante! Risata: OH... OH... OH...',
        "racconto": """C'era una volta un Elefante di nome Franco, che gli amici chiamavano ... EleFranco. Di cognome faceva Franchini.

Abitava nella sua casa a FrancaVilla, una cittadina fluviale costruita su palafitte e ponti di corda intrecciata, dove l'acqua scorreva placida sotto i pavimenti di legno, le barche colorate facevano da bizzarri taxi tra una casa e l'altra e i panni stesi sventolavano sopra il fiume.

Quel mattino era finalmente uscito il nuovo numero del fumetto di "Super-Elefante", il suo preferito. «Non posso perdermelo, devo correre all'edicola prima che finiscano le copie!» esclamò EleFranco tutto eccitato. Si infilò i suoi stivali giganti lucidi ed uscì. Il pavimento di legno della passerella vibrava ritmicamente sotto di lui: THUMP THUMP THUMP.

Presso un grande albero del parco, sentì dei piccoli mugolii tremanti. Alzò lo sguardo e vide Betta la Scimmietta, piccola e infreddolita, che batteva i dentini rannicchiata su un ramo basso, fissando disperata qualcosa più in alto.

«Brrr, EleFranco, che freddo!» tremò Betta. «Un colpo di vento mi ha portato via la mia sciarpa rossa, quella che mi teneva calda, e l'ha lanciata su quel ramo altissimo lassù! Io non riesco ad arrampicarmi così in alto, è troppo sottile e pericoloso, e senza la sciarpa sto gelando tutta!»

«Non tremare, Betta, la tua sciarpa te la riprendo io,» disse EleFranco guardando in su con aria sicura.

Ma poi pensò al suo fumetto e la mente cominciò a vagare: si mise a immaginare quali nuovi superpoteri avrebbe usato Super-Elefante in questo numero, se ci sarebbe stato il suo nemico storico e quanto fossero colorate e spettacolari le vignette.

Si stava distraendo, ma vedendo Betta soffrire il freddo, scosse le orecchie e gridò: "FOCUS!"

«Tieni duro un secondo, piccola, ci arrivo io fin lassù,» la rassicurò.

Si alzò in piedi sulle zampe posteriori, in bilico, e cominciò ad allungare la proboscide verso l'alto, sempre più su, tendendola al massimo con tutte le sue forze per raggiungere quel ramo lontanissimo. Tese, tese ancora, si stiracchiò fino al limite e — SCRACK! — la schiena gli fece un rumore pazzesco e rimase bloccato in quella posizione storta, paralizzato dal dolore. Ma con la punta della proboscide riuscì comunque ad agganciare la sciarpa rossa e a riportarla, calda e morbida, intorno al collo di Betta.

«Grazie, EleFranco, sei il mio eroe!» squittì la scimmietta, finalmente al calduccio. E proprio mentre lo diceva, notò un vecchio foglio di carta colorato impigliato tra le foglie del ramo. Lo afferrò e lo lanciò giù all'elefante: «Tieni, questo è per te!»

EleFranco lo raccolse e quasi gli si bloccò di nuovo la schiena dalla sorpresa: era la rarissima pagina centrale inedita proprio del fumetto di "Super-Elefante", quella con il poster gigante, volata via dall'edicola il giorno prima a causa del vento! Adesso la sua collezione era completa, anzi, più completa di chiunque altro.

«Sono io il vero Super-Elefante!» esclamò ridendo, mentre con un piacevole "click" la schiena si rimetteva a posto da sola. La missione era compiuta, e in modo eroico!

EleFranco si sbloccò dalla gioia e partì con la sua conosciutissima risata: OH... OH... OH...""",
    },
    {"num": 17,
        "title": '🪵 In Falegnameria per la Sedia e Lendo il Topo Tremendo 🐭',
        "missione": 'EleFranco va dal falegname del paesino a riparare una gamba dondolante della sua sedia preferita. 🪑',
        "incontro": "Trova Lendo il Topo Tremendo, un topolino vivace ma disperato perché ha combinato un pasticcio: per fare uno scherzo ha rosicchiato e fatto crollare l'insegna di legno della biblioteca del paesino, che ora blocca l'ingresso principale. 📚",
        "aiuto": 'EleFranco usa la sua incredibile forza per sollevare la pesante insegna e tenerla ferma contro la parete. Lo sforzo prolungato a braccia tese gli fa accumulare così tanta segatura e polvere di legno sulla schiena da farlo prudere tutto. 🪵',
        "morale": 'Riparare agli errori altrui riporta l\'ordine e trasforma un "tremendo" pasticcio in una buona azione. 🤝',
        "colpo": "Lendo, pentito e grato, usa i suoi dentini affilati per intagliare al volo un perfetto cuneo di legno duro dai resti dell'insegna. Lo infila sotto la gamba della sedia di EleFranco, riparandola all'istante meglio del falegname. 🛠",
        "finale_schema": 'La sedia è perfettamente stabile senza andare in officina! E via di risata: OH... OH... OH...',
        "racconto": """C'era una volta un Elefante di nome Franco, che gli amici chiamavano ... EleFranco. Di cognome faceva Franchini.

Abitava nella sua accogliente casa all'interno del paesino di FrancaVilla, un borgo laborioso dove dalle botteghe usciva profumo di legno e di trucioli, le insegne intagliate dondolavano sopra le porte e il fiume faceva girare pigramente la ruota di un vecchio mulino.

Un mattino, mentre faceva colazione, EleFranco si sedette sulla sua sedia di legno preferita e... crack! Quasi cadde all'indietro: una delle gambe posteriori si era accorciata e dondolava paurosamente. «Accidenti, per poco non finivo a gambe all'aria!» esclamò rialzandosi. «Devo andare subito alla falegnameria di FrancaVilla a farla sistemare.» Si infilò i suoi stivali giganti di cuoio scuro, si caricò la sedia sotto il braccio e uscì di casa con passo deciso. La strada sterrata risuonava al solito ritmo: THUMP THUMP THUMP.

Davanti alla biblioteca del paese trovò una gran confusione e un topolino in lacrime accanto a un enorme cartello di legno rovesciato. Era Lendo il Topo Tremendo, vivace e dispettoso, ma in quel momento dispiaciutissimo, con i baffetti che tremavano per il pianto.

«È tutta colpa mia, EleFranco!» squittì Lendo asciugandosi una lacrima. «Volevo fare uno scherzo e ho rosicchiato i sostegni dell'insegna di legno della biblioteca... ma ho esagerato e l'insegna è crollata di schianto, bloccando tutta la porta d'ingresso! Adesso nessuno può entrare a prendere i libri e io non so proprio come rimediare al pasticcio che ho combinato!»

«Su, Lendo, gli errori si possono sempre riparare,» lo consolò EleFranco. «Adesso vediamo come sistemare le cose.»

Ma poi guardò la sua sedia dondolante e la mente cominciò a vagare: si mise a pensare a che tipo di colla avrebbe usato il falegname, se quella forte alla resina di pino, e se avrebbe dovuto lasciare lì la sedia per giorni interi.

Si stava perdendo in questi pensieri, ma vedendo Lendo così pentito e in lacrime, scosse le orecchie e gridò: "FOCUS!"

«Niente paura, piccolo, quell'insegna la rimettiamo a posto noi due,» disse rimboccandosi le maniche.

Con la sua forza straordinaria, EleFranco afferrò la pesantissima insegna di legno e la sollevò di netto, riposizionandola dritta contro il muro della biblioteca. Poi la tenne ferma, a zampe tese e muscoli in tensione, mentre Lendo correva a cercare chiodi e martello per fissarla. I minuti passavano e l'elefante non mollava la presa, anche se una fastidiosa pioggia di segatura e polvere di legno gli cadeva di continuo sulla schiena, facendogli venire un prurito pazzesco. «Resisti... resisti...» si ripeteva, fremendo dal solletico ma immobile come una colonna.

Quando finalmente l'insegna fu inchiodata di nuovo al suo posto, EleFranco poté spostarsi e grattarsi a dovere. Lendo, grato e desideroso di farsi perdonare, corse verso i pezzetti di legno duro avanzati e, con i suoi dentini affilati e precisi, intagliò al volo un cuneo perfetto. Poi lo infilò sotto la gamba corta della sedia di EleFranco, calzandolo alla perfezione: la sedia smise di dondolare e tornò stabile e solida, riparata meglio di come avrebbe fatto il falegname!

«Provala!» squittì Lendo. EleFranco si sedette: non un dondolio, non uno scricchiolio. La missione era compiuta senza nemmeno entrare in officina, e un "tremendo" pasticcio si era trasformato in una buona azione.

EleFranco si sedette felice e scoppiò nella sua famosa risata: OH... OH... OH...""",
    },
    {"num": 18,
        "title": "🎨 Dal Colorificio per le Vernici e Morno l'Unicorno 🦄",
        "missione": 'EleFranco va al colorificio a comprare un barattolo di vernice celeste per ridipingere la staccionata di casa sua. 🖌',
        "incontro": "Incontra Morno l'Unicorno, una creatura magica ma tristissima perché camminando nella nebbia mattutina ha perso tutto il luccichio del suo manto bianco e il suo corno magico non brilla più, facendolo sentire comune e invisibile. 🌫",
        "aiuto": "EleFranco strofina delicatamente il manto di Morno usando la punta morbida della sua proboscide per asciugarlo. Ma l'energia statica generata dallo sfregamento fa accumulare tutta la nebbia umida intorno a EleFranco, facendolo starnutire e riempiendolo di goccioline. 💦",
        "morale": 'La vera magia splende quando ci prendiamo cura della bellezza di chi amiamo. ✨',
        "colpo": "Il calore dell'amicizia riaccende improvvisamente il potere di Morno: il suo corno lancia un raggio di luce arcobaleno scintillante che colpisce la staccionata di EleFranco, colorandola di sfumature celeste e magiche che brillano al sole. 🌈",
        "finale_schema": 'Staccionata dipinta di pura magia senza bisogno di comprare vernici! Risata: OH... OH... OH...',
        "racconto": """C'era una volta un Elefante di nome Franco, che gli amici chiamavano ... EleFranco. Di cognome faceva Franchini.

Abitava nella sua casa a FrancaVilla, una graziosa cittadina circondata da canali e ponticelli fioriti, dove l'aria profumava di lavanda, i mulini a vento giravano dolcemente all'orizzonte e ogni mattina una soffice nebbia argentata avvolgeva i sentieri.

Quel giorno EleFranco notò che la staccionata del suo giardino era tutta sbiadita e scrostata. «Così è proprio triste,» disse passandoci una zampa. «Andrò subito al colorificio a comprare un bel barattolo di vernice celeste per rinfrescarla.» Si infilò le sue scarpe giganti ed uscì di casa. Mentre camminava lungo il sentiero avvolto dalla nebbia mattutina, la terra risuonava: THUMP THUMP THUMP.

Vicino a un cespuglio bagnato di guazza, sentì un singhiozzo malinconico. Si avvicinò e, tra la foschia, scorse una creatura meravigliosa ma sconsolata: Morno l'Unicorno, dal manto che un tempo doveva essere candido e luminoso, ora opaco e grigiastro, con le orecchie abbassate e il corno spento sulla fronte.

«Oh, EleFranco,» sospirò Morno con voce tremante. «Camminando in questa nebbia umida il mio manto magico si è tutto inzuppato e ha perso il suo luccichio. E senza il bagliore, il mio corno non brilla più nemmeno un pochino! Mi sento spento, comune e invisibile, come se nessuno potesse più vedermi. Un unicorno che non brilla, che unicorno è?»

«Non dire così, Morno, la tua magia è solo un po' bagnata, mica sparita,» lo confortò EleFranco con dolcezza.

Ma poi pensò alla sua staccionata e la mente cominciò a vagare: si mise a chiedersi quanti pennelli avrebbe dovuto comprare, quale sfumatura di celeste scegliere — quello cielo o quello acquamarina? — e se servisse anche una scala per arrivare in cima ai pali.

Si stava perdendo in questi dettagli, ma vedendo una lacrima scivolare lungo il muso di Morno, scosse la testa e gridò: "FOCUS!"

«Vieni qui, amico, ti asciugo io e vedrai che tornerai a splendere,» gli promise.

Cominciò a strofinare delicatamente il manto dell'unicorno con la punta morbida della proboscide, asciugando ciocca dopo ciocca con movimenti circolari e pazienti. Ma quello sfregamento continuo generò una gran quantità di elettricità statica che, come una calamita, attirò tutta la nebbia umida dei dintorni proprio addosso all'elefante! In un attimo EleFranco si ritrovò avvolto in una nuvoletta tutta sua, fradicio di goccioline e con un solletico al naso irrefrenabile: «ETCIÙ! Etciù! Pfff, quanta acqua!» starnutiva senza sosta.

Ma non si arrese e continuò a strofinare finché il manto di Morno non fu perfettamente asciutto e morbido. E allora accadde la magia: il calore di quell'amicizia sincera riaccese di colpo il potere dell'unicorno. Il suo corno tornò a brillare e lanciò un potente raggio di luce arcobaleno scintillante che, attraversando i giardini, colpì dritto la vecchia staccionata di EleFranco, dipingendola all'istante di mille sfumature di celeste magico e luccicante, più bella di qualunque vernice in commercio!

«Guarda che meraviglia!» esclamò Morno, di nuovo splendente. La staccionata brillava al sole e la missione era compiuta senza spendere un soldo.

EleFranco alzò la proboscide e inondò tutti con la sua famosa risata: OH... OH... OH...""",
    },
    {"num": 19,
        "title": '🥦 Dal Fruttivendolo e Lattuga la Tartaruga 🐢',
        "missione": "EleFranco deve andare dal fruttivendolo a comprare un bel cespo di lattuga romana croccante per l'insalata di pranzo. 🥬",
        "incontro": 'Incontra Lattuga la Tartaruga, disperata sul sentiero perché ha un problema fastidioso col suo carapace: si è incastrata al contrario dentro un vecchio secchiello di plastica abbandonato e non riesce più a muoversi. 🪣',
        "aiuto": "EleFranco tenta di sfilarla con la proboscide, ma il secchiello è troppo stretto. Allora decide di fare leva usando delicatamente la punta della zampa gigante. Nel farlo, l'effetto molla fa volare via il secchiello, ma un grande spruzzo di acqua e fango accumulato nel secchio finisce dritto sul ciuffo di capelli di EleFranco, spettinandolo tutto. 🌀",
        "morale": 'Anche quando un problema sembra una prigione stretta, con la giusta leva e un briciolo di pazienza si ritrova la libertà. 🐢',
        "colpo": 'Il secchiello volando va a colpire un vecchio albero selvatico, facendo cadere a terra un cesto pieno di verdure fresche e una gigantesca lattuga croccante che rotola dritta tra le zampe di EleFranco. 🧺',
        "finale_schema": "L'insalata per il pranzo è pronta senza camminare fino al negozio! Risata: OH... OH... OH...",
        "racconto": """C'era una volta un Elefante di nome Franco, che gli amici chiamavano ... EleFranco. Di cognome faceva Franchini.

Abitava nella sua accogliente casa all'interno del paesino di FrancaVilla, un borgo da fiaba adagiato in una radura fiorita dove le stradine erano fatte di sassolini rosa e le siepi di mirtillo crescevano così ordinate da sembrare disegnate con il righello.

Quella mattina il suo stomaco reclamava qualcosa di verde: «Andrò subito dal fruttivendolo Pino a prendere un cespo di lattuga romana gigante per il pranzo» decise. Si infilò i suoi stivali giganti di gomma verde brillante, aprì la porta di casa e si mise in marcia. Mentre avanzava sul sentiero, la terra risuonava dolcemente: THUMP THUMP THUMP.

Fu a metà del cammino, vicino a un cespuglio di ortiche, che notò qualcosa di strano. C'era un vecchio secchiello di plastica colorato capovolto, e da sotto spuntavano quattro zampette che scalciavano freneticamente a vuoto. Avvicinandosi, sentì una vocina soffocata: «Aiuto! Qualcuno tolga questo guscio finto dal mio guscio vero!» Era Lattuga la Tartaruga, che camminando distratta si era infilata dentro il secchiello abbandonato e ora il suo carapace era completamente incastrato. Non riusciva né ad andare avanti né a girarsi.

«Sta' tranquilla, Lattuga, fuori da quel secchio ti ci tiro io,» la rassicurò EleFranco con voce calma.

Ma poi si fermò ad osservarla e iniziò a pensare a quante foglie avesse la lattuga da comprare, se condirla con un pizzico di sale o con due gocce di limone e a quanto fosse croccante il torsolo.

Si stava proprio perdendo in questi pensieri culinari, ma un piccolo pianto di Lattuga lo riscosse dal torpore.

Scosse le grandi orecchie e gridò forte: "FOCUS!"

«Eccomi, piccola amica, niente paura: ti libero piano piano,» le disse inginocchiandosi di fianco.

Allungò la proboscide e provò ad afferrare il secchiello per sfilarlo, ma la plastica faceva attrito sul carapace ruvido e non si muoveva di un millimetro. Lattuga gridava per il solletico e per la paura. EleFranco allora capì che serviva una strategia diversa: doveva fare leva. Posizionò con estrema cura la punta della sua zampa anteriore gigante contro il bordo del secchiello, calcolando la forza per non schiacciare la piccola amica. Spingendo millimetro dopo millimetro, tese i muscoli e fece pressione. All'improvviso... SLING! La plastica cedette e il secchiello volò via in aria come un proiettile a molla. Ma nel secchiello si era accumulata della vecchia acqua piovana mista a terra: lo strato di fango liquido schizzò dritto in faccia a EleFranco, prendendolo in pieno sul ciuffetto di capelli in testa, che si ammosciò completamente coprendogli gli occhi.

EleFranco non ci vedeva più nulla, ma Lattuga era finalmente libera e camminava felice sul sentiero.

Mentre EleFranco cercava di pulirsi i capelli con la proboscide, il secchiello, che stava ancora volando alto nel cielo di FrancaVilla, andò a sbattere contro il ramo di un grande orto pensile selvatico. L'impatto fu così forte che fece cadere una cassetta dimenticata lassù: la cassetta si rovesciò e un cespo gigantesco di lattuga romana, verde, freschissima e bagnata di rugiada, rotolò giù per la collina fermandosi precisamente contro gli stivali dell'elefante.

La merenda salutare era pronta e Lattuga era salva, senza camminare fino al negozio!

EleFranco si ripulì il ciuffo e scoppiò nella sua famosa risata: OH... OH... OH...""",
    },
    {"num": 20,
        "title": "👑 Al Palazzo Reale e Regina l'Ape 🐝",
        "missione": 'EleFranco deve andare a consegnare un pacco di zucchero di canna al Palazzo Reale per le cucine della regina. 📦',
        "incontro": "Vicino ai giardini della corte incontra Regina l'Ape, la regina dell'alveare reale, sdraiata a pancia in su sopra una rosa, che si lamenta stringendosi le zampette sulla pancia perché ha fatto una tremenda indigestione di pappa reale. 🍯",
        "aiuto": 'EleFranco, sapendo che per digerire serve muoversi, posiziona Regina sulla sua proboscide e inizia a dondolarla delicatamente su e giù a ritmo di valzer, come se fosse sulle montagne russe del parco giochi. Ma il dondolio continuo, unito al profumo dolce della pappa reale, fa venire un giramento di testa pazzesco proprio a EleFranco, che inizia a camminare ondeggiando come una nave in mezzo alla tempesta. 🌀',
        "morale": 'Anche i dolci più prelibati perdono il loro valore se esageriamo: la giusta misura è il segreto della vera felicità. ⚖',
        "colpo": "Il movimento ondeggiante di EleFranco fa cadere accidentalmente il pacco di zucchero che aveva in spalla, il quale si rompe versandosi su un grande limone selvatico caduto a terra. Regina l'Ape, stando meglio grazie ai volteggi, suggerisce di unire lo zucchero e il limone con l'acqua della fontana, creando una limonata digestiva eccezionale per entrambi. 🍋",
        "finale_schema": 'Il mal di pancia è passato e la consegna è avvenuta direttamente nei giardini reali! Risata: OH... OH... OH...',
        "racconto": """C'era una volta un Elefante di nome Franco, che gli amici chiamavano ... EleFranco. Di cognome faceva Franchini. Abitava nella sua accogliente casa all'interno del paesino di FrancaVilla, una cittadina maestosa dove le piazze erano ornate da grandi statue di pietra e le fontane zampillavano acqua limpida che rinfrescava l'aria profumata di lavanda.

Quel giorno aveva un compito importante: doveva trasportare un pesante sacco di zucchero di canna fino alle grandi cucine del Palazzo Reale. «La torta del Re ha bisogno di questo ingrediente, devo sbrigarmi» pensò. Si infilò i suoi stivali giganti di cuoio lucido per l'occasione elegante, si caricò il sacco sulla spalla e uscì. Camminava fiero lungo il viale alberato che portava alla corte: THUMP THUMP THUMP Arrivato nei pressi della grande cancellata d'oro dei giardini reali, sentì un gemito provenire da una grande rosa scarlatta.

Si sporse e vide Regina l'Ape, la sovrana di tutti gli alveari del regno. Regina era sdraiata sulla schiena, con le coroncina tutta storta e le sei zampette strette intorno alla pancia gonfia. «Oh, EleFranco, che sofferenza!» gemette. «Le mie api operaie mi hanno preparato un vassoio pieno di pappa reale freschissima e io... beh, ne ho mangiata decisamente troppa!

Ho un mal di pancia così forte che non riesco nemmeno a muovere le ali.» EleFranco guardò le finestre del palazzo. Iniziò a pensare a che sapore avesse la glassa della torta reale, se il pasticcere di corte usasse i canditi e a quanti piani fosse alto il dolce del Re. Si stava proprio lasciando distrarre da quei pensieri di zucchero, ma un forte lamento dell'ape lo riportò al dovere.

Scosse le grandi orecchie e gridò: "FOCUS!" Sapeva che per curare l'indigestione non servivano medicine, ma un buon movimento. Fece salire Regina l'Ape sulla punta della sua proboscide e, tenendola ben salda, iniziò a muoverla delicatamente descrivendo dei grandi cerchi nell'aria a ritmo di musica, imitando le montagne russe. *"Su e giù, a destra e a sinistra!"* faceva EleFranco per aiutare lo stomaco dell'ape a lavorare. Continuò per lunghissimi minuti, facendo fare a Regina dei volteggi perfetti. Ma a forza di girare la proboscide in tondo e di respirare il profumo dolciastro e intenso della pappa reale, la testa iniziò a girare vorticosamente... a EleFranco!

L'elefante perse l'equilibrio e iniziò a camminare ondeggiando paurosamente da una parte all'altra della via, proprio come una barchetta in mezzo a un mare in tempesta, rischiando di cadere. A causa di quel buffo ondeggiamento, il grande sacco di zucchero gli scivolò dalla spalla e cadde a terra, rompendosi e rovesciando il contenuto sopra un enorme limone selvatico che era caduto dall'albero del giardino. Regina l'Ape, che grazie ai volteggi sentiva la pancia finalmente sgonfia e leggera, volò giù e vide la scena: «EleFranco, guarda! La natura ci ha dato la soluzione!

Uniamo lo zucchero e il succo di quel limone con l'acqua fresca della fontana del re!» Con la proboscide, EleFranco spremette il limone e mescolò il tutto, creando una fantastica e rinfrescante limonata digestiva che curò all'istante il giramento di testa dell'elefante. Lo zucchero era consegnato e il banchetto era salvo!

EleFranco si riprese, guardò la sua nuova amica e lanciò la sua famosa risata: OH... OH... OH...""",
    },
    {"num": 21,
        "title": '☁ In Edicola per le Notizie e Lalla la Farfalla Unicorno 🦄🦋',
        "missione": "EleFranco deve andare all'edicola del paesino a comprare il giornale del mattino per leggere le notizie di FrancaVilla. 📰",
        "incontro": "Guardando in alto verso la collina nebbiosa, scorge Lalla la Farfalla Unicorno (una farfalla magica con un piccolo corno lucente sulla testa), bloccata sopra una nuvola bassa che si è impigliata sulla cima di un grande campanile. Lalla piange perché è volata fin lassù inseguendo una scia di polline, ma ora si è accorta di quanto sia alto il campanile ed è rimasta paralizzata dalla vertigine e dalla paura dell'altezza.",
        "aiuto": "EleFranco, per farle superare la paura, decide di arrampicarsi sulla scalinata esterna del campanile. Arrivato in cima, tese la proboscide per farla scendere, ma per convincerla deve iniziare a farle vedere che sotto di loro il paesino sembra piccolissimo e divertente, come un set di mattoncini Lego. Ma proprio mentre si sporge per indicarle le casette, un colpo di vento fa volare via il cappello di EleFranco, che cade giù, costringendo l'elefante a fare uno sforzo immenso per rimanere in equilibrio sulla ringhiera stretta. 🌪",
        "morale": "La paura dell'altezza si sconfigge non guardando il vuoto, ma concentrandosi sulla bellezza del panorama e sulla mano tesa di chi ci vuole bene. 🌲",
        "colpo": "Lalla, vedendo l'elefante in difficoltà, si dimentica della sua paura: spicca il volo, scende in picchiata a recuperare il cappello al volo nel vuoto e lo riporta a EleFranco, atterrando poi dolcemente sulla sua testa. Nel farlo, le sue ali magiche lasciano cadere una scia di polline dorato che si deposita su una copia del giornale volata via dall'edicola e impigliatasi sul campanile il giorno prima. 📰",
        "finale_schema": 'Il giornale del mattino è recuperato direttamente in cima al campanile e Lalla ha sconfitto la vertigine! Risata di gioia: OH... OH... OH...',
        "racconto": """C'era una volta un Elefante di nome Franco, che gli amici chiamavano ... EleFranco. Di cognome faceva Franchini. Abitava nella sua accogliente casa all'interno del paesino di FrancaVilla, una contrada suggestiva costruita ai piedi di una montagna antica, dove le case avevano facciate color pastello e i campanili svettavano alti nel cielo, bucando le nuvole mattutine che sembravano panna montata.

Quella mattina voleva aggiornarsi: «Andrò all'edicola della piazza a comprare il giornale per leggere cosa succede nel mondo» pensò. Si infilò i suoi stivali giganti da passeggio leggeri, aprì la porta di casa e si mise in cammino. Sulla strada i suoi piedoni producevano un suono rassicurante: THUMP THUMP THUMP Arrivato vicino alla vecchia torre del campanile, alzò gli occhi e vide una scena insolita. Lassù, sopra una nuvola soffice rimasta incastrata tra le campane di pietra, c'era Lalla la Farfalla Unicorno, una creatura rarissima con ali di velluto sfumato e un piccolo corno scintillante sulla fronte.

Lalla stava piangendo disperata: era volata fin lassù seguendo un profumo di fiori di montagna, ma guardando in basso si era accorta di quanto fosse alto il campanile e la vertigine l'aveva completamente paralizzata. Aveva troppa paura dell'altezza per spiegare le ali e scendere. EleFranco rimase a guardare la cima della torre. Iniziò a pensare a quante pagine di fumetti ci fossero nel giornale, se ci fossero la pagina dei giochi con i cruciverba e se l'edicolante avesse finito le figurine degli elefanti calciatori.

Si stava lasciando distrarre da questi pensieri di carta, ma un singhiozzo spaventato di Lalla lo riportò al presente. Scosse le grandi orecchie e gridò forte verso l'alto: "FOCUS!" Deciso ad aiutarla, EleFranco iniziò a salire i gradini della ripida scalinata esterna del campanile. Gradino dopo gradino, faticando per la sua stazza, arrivò finalmente sulla terrazza della cima, proprio all'altezza della nuvola. Tese la sua lunga proboscide verso la farfalla come se fosse un ponte sicuro e, per farle passare lo spavento, iniziò a parlarle con dolcezza: «Guarda giù, Lalla, ma non guardare il vuoto!

Guarda le casette di FrancaVilla: da qui sembrano piccolissime, sembrano fatte di Lego colorati! E le macchinine sembrano scarafaggi che corrono!» EleFranco si sporse molto sulla ringhiera di pietra per indicarle un bizzarro tetto rosso. Ma proprio in quel momento, una fortissima folata di vento colpì la cima del campanile, sollevando il cappello di EleFranco e facendolo volare nel vuoto.

L'elefante, preso alla sprovvista, perse l'equilibrio e dovette fare uno sforzo immenso con i muscoli delle zampe posteriori, dondolandosi sulla ringhiera stretta per non cadere di sotto. Era in serio pericolo! Lalla la Farfalla Unicorno, vedendo il suo grande salvatore sul punto di cadere, provò una scarica di coraggio che le fece dimenticare ogni vertigine. Spiegò le ali colorate, si tuffò dalla nuvola e scese in una picchiata velocissima nel vuoto, acchiappando il cappello al volo un attimo prima che toccasse terra.

Con un colpo d'ala elegante, risalì leggera verso la cima del campanile e posò il cappello sulla testa di EleFranco, atterrando poi dolcemente sul suo ciuffo. Nel muovere le ali per frenare, Lalla lasciò cadere una scia di polline d'oro magico: il polline illuminò una fessura della pietra dove si era incastrata una copia perfetta e intatta del giornale del mattino, volata via dall'edicola il giorno prima per via del vento! La missione era compiuta direttamente in cima alla torre. La farfalla non aveva più paura del vuoto ed EleFranco aveva il suo giornale.

Felice, l'elefante si mise comodo e lanciò la sua famosa risata: OH... OH... OH...""",
    },
]
