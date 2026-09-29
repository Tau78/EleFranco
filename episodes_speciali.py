"""Episodi speciali Iris Edition — capitoli fuori numerazione stagionale.

Ogni speciale usa ``num`` >= 1001 (es. 1001, 1002…) e ``insert_after`` per fissare
l'ordine di lettura rispetto ai capitoli canonici (es. ``insert_after: 25`` =
subito dopo l'Ep. 25). Campi aggiuntivi: ``special_id`` (es. ``"S1"``).

Modifica qui e rigenera con ``python3 aggiorna_libro.py``.
"""

from __future__ import annotations

SPECIAL_EPISODES: list[dict] = [
    {
        "num": 1001,
        "special_id": "S1",
        "insert_after": 25,
        "title": "❄ FrancaVilla d'Inverno e Fred il Castoro 🦫",
        "missione": (
            "EleFranco deve andare al deposito di legna sul ciglio del bosco a prendere "
            "fascine di abete profumato per il camino della Festa d'Inverno di Franca, "
            "prima che il sole cali e il gelo chiuda le botteghe del borgo. 🔥"
        ),
        "incontro": (
            "Sul ponticello ghiacciato del fiume incontra Fred il Castoro, disperato: "
            "la diga d'inverno che proteggeva la tana degli scoiattoli si è trasformata "
            "in un muro di ghiaccio fragile e sta cedendo sotto la corrente gelida, "
            "minacciando l'albero-casa sotto la riva. 🦫"
        ),
        "aiuto": (
            "EleFranco sposta blocchi di ghiaccio con la proboscide e frena la corrente "
            "con le zampe come uno scudo, ma scivola sulla riva innevata, innesca una "
            "valanga di neve che gli copre la proboscide e resta bloccato tra tronchi "
            "ghiacciati — la missione legna sembra perduta. 🧊"
        ),
        "morale": "Nel freddo più forte, la comunità scalda chi si aiuta a vicenda. 🔥",
        "colpo": (
            "Gli scoiattoli della diga sbucano dalla casetta-albero con legna secca e "
            "rametti profumati che avevano conservato; il vento caldo dai camini di "
            "FrancaVilla e la diga riparata da Fred deviano l'acqua nel posto giusto — "
            "fascine pronte senza passare dal deposito. 🐿"
        ),
        "finale_schema": (
            "La Festa d'Inverno di Franca è pronta, camino acceso! E via di risata: "
            "OH... OH... OH..."
        ),
        "racconto": """C'era una volta un Elefante di nome Franco, che gli amici chiamavano ... EleFranco. Di cognome faceva Franchini.

Abitava nella sua accogliente casa nel paesino di FrancaVilla, che in quel periodo dell'anno era diventata un borgo d'inverno incantato: i tetti portavano cappelli bianchi di neve, i camini sbuffavano nuvole calde, dai grondaiali pendevano ghiaccioli trasparenti e dalle finestre illuminate si vedevano tavoli apparecchiati e luci dorate. L'aria sapeva di legna arsa, cannella e pane appena sfornato.

Era un pomeriggio di gelo gentile e EleFranco aveva un compito urgentissimo: «Stasera è la Festa d'Inverno di Franca! Devo portare fascine di abete profumato per il suo camino. Senza fuoco caldo, niente Festa accogliente!» Guardò il cielo che arrossava verso sera: «Meglio sbrigarsi, prima che il gelo chiuda le botteghe.»

Si infilò i suoi stivali giganti foderati di lana, prese una corda robusta e uscì di casa. Mentre percorreva la strada innevata verso il bosco, la terra tremava piano: THUMP THUMP THUMP.

Arrivato vicino al ponticello sul fiume — lo stesso della prima avventura con Fred — sentì scricchioli e gorgoglii gelidi. Sulla riva, un castoro dalla pelliccia lucida e dai grandi denti color avorio correva avanti e indietro tenendosi la testa tra le zampe. Era Fred il Castoro, il più bravo costruttore di tutta FrancaVilla, e quella sera piangeva disperato.

«EleFranco, è una catastrofe!» singhiozzò Fred. «La mia diga d'inverno sta cedendo! L'ho rinforzata con tronchi e ghiaccio, ma stanotte il fiume è cresciuto sotto il gelo e ora si sfaldano come grissini! Se crolla, l'acqua gelida allagherà la mia tana e perfino l'albero-casa degli scoiattoli che dormono là sotto. Ho lavorato per settimane!»

«Respira, Fred,» disse EleFranco con voce calda come una coperta al sole. «Ci sono qui io adesso, come quando abbiamo salvato la diga la prima volta.»

Ma poi, guardando i blocchi di ghiaccio che scintillavano al tramonto, la sua mente cominciò a vagare. Pensò alle fascine del deposito — quante ne servivano? — e alla Festa d'Inverno di Franca: rametti sull'ingresso, tisane calde per tutti...

Stava quasi per perdersi del tutto in quei pensieri quando Fred lanciò un urlo lacerante: «EleFranco, sta crollando TUTTO! Guarda l'albero-casa!»

Allora l'elefante scosse le grandi orecchie e disse ad alta voce la sua parola magica: "FOCUS!"

«Tieni duro, Fred, la tua diga la salviamo insieme!» gridò, e passò all'azione. Piantò le zampe massicce contro la corrente gelida come un enorme scudo. Poi, con la proboscide, spostò blocchi di ghiaccio e incastrò tronchi nei punti più fragili, tappando ogni falla come aveva fatto con il fango argilloso mesi prima.

Lavorò senza fermarsi mai, mentre Fred gli passava rametti e foglie resinose. «Un po' più a sinistra! Ecco, lì! Sei fortissimo anche col freddo!» lo incoraggiava il castoro. Pezzo dopo pezzo, la diga cominciò a reggere. Ma la riva era coperta di ghiaccio sottile: un passo falso, e EleFranco scivolò con un tonfo comicissimo, sollevando una valanga di neve che gli ricoprì la proboscide da punta a punta.

«Bleah!» fece EleFranco, scuotendosi come un albero innevato.

Nel tentativo di rialzarsi, spinse un blocco di ghiaccio troppo grande: CRAC! Il blocco rotolò verso il ponticello e bloccò il sentiero che portava al deposito di legna. EleFranco restò incastrato tra due tronchi ghiacciati, con la corda impigliata e la proboscide ancora bianca come una torcia di neve.

«Oh no,» mormorò. «Il deposito è dall'altra parte del fiume, il sentiero è bloccato, e la Festa d'Inverno di Franca inizia tra poco. Le ho rovinato il camino...»

Fred si avvicinò, trascinando la coda sul ghiaccio. «EleFranco, tu hai salvato la nostra diga. Gli scoiattoli ti devono una grande gratitudine.»

Proprio in quel momento, dall'albero-casa sbucarono gli scoiattoli che Fred aveva protetto fin dalla prima diga — quelli che un tempo avevano regalato nastri e dolci di noci per la Festa di Franca.

«Per te, EleFranco!» squittirono in coro. «Hai salvato la nostra casa ancora una volta!»

Scivolarono giù portando fascine di legna secca e rametti profumati conservati nell'attico dell'albero fin dall'autunno. La legna era asciutta e profumava di resina — perfetta per un camino di Festa.

Un soffio caldo arrivò dai camini accesi di FrancaVilla. Quel tepore incontrò la diga riparata, l'acqua deviò nel canale di Fred e il sentiero del ponticello si liberò appena. EleFranco caricò le fascine sulla corda e riprese il cammino.

Sulla soglia, Franca lo aspettava con il grembiule a pois e una corona di pigne dorate. «Sei arrivato! Il camino è pronto, mancava solo la legna!»

Dentro, la Festa d'Inverno era già viva. Otto il Coniglietto sorseggiava una tisana calda con la sua copertina di lana. Iris, la stessa bambina gentile del giardino, con le trecce e il grembiule a fiori, sistemava rametti di abete sul tavolo. Fred entrò seguito dagli scoiattoli con noci tostate per tutti.

EleFranco posò le fascine nel camino, il fuoco crepitò allegro e la stanza si riempì di luce arancione e odore di abete. La missione era compiuta senza nemmeno arrivare al deposito: Franca avrebbe avuto la Festa d'Inverno più calda del mondo!

Si tolse un fiocco di neve dal ciuffo, guardò gli amici riuniti e scoppiò nella sua famosa risata: OH... OH... OH...""",
    },
]
