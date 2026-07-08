"""English image prompts for all EleFranco episodes (A–D format)."""

NEGATIVE_PROMPT = (
    "text, letters, words, watermark, logo, signature, realistic photo, scary, violent, "
    "blood, weapons, adult themes, dark horror, distorted anatomy, extra limbs, blurry face, "
    "low quality, cropped head, modern city skyline, screens and phones"
)

STYLE = (
    "soft watercolor children's book illustration, warm gentle flat colors, rounded friendly "
    "shapes, A4 portrait composition, bedtime story mood, Iris Edition, no text in image"
)

BASE = (
    "large generous friendly cartoon elephant EleFranco with small black hair tuft on head"
)

SECTION_PROMPTS = {
    "cover": (
        f"{BASE}, giant brown leather boots, standing proudly in the charming square of "
        "FrancaVilla at golden hour, gingerbread rooftops and soft chimney smoke, warm "
        f"welcoming smile, {STYLE}"
    ),
    "parte_1": (
        f"{BASE}, giant boots, leaving cozy home at morning in marzipane-roofed FrancaVilla, "
        "wicker shopping basket, light dust rising THUMP THUMP on cobblestone path, "
        f"{STYLE}"
    ),
    "parte_2": (
        f"{BASE}, giant work boots, artisan village FrancaVilla with colorful workshops, "
        f"helping small animal friends amid comic mishaps, warm adventurous tone, {STYLE}"
    ),
    "parte_3": (
        f"{BASE}, green rubber giant boots, agricultural FrancaVilla with vegetable fields "
        f"and windmills, meeting new small friends, spring morning light, {STYLE}"
    ),
    "disegna": (
        "Clean black line art coloring page for children, simple bold outlines, no fill, "
        "no shading, EleFranco elephant with hair tuft and giant boots, FrancaVilla scene "
        "matching chapter theme, print-friendly A4 portrait, no text"
    ),
    "disegna_slide": (
        f"{BASE}, colorful patchwork cape, giant brown leather boots, holding crayons and "
        "paint palette, sitting on grass with small animal friends coloring large paper "
        "sheets together, whimsical FrancaVilla gingerbread rooftops in soft background, "
        f"joyful creative mood, bold clean cartoon outlines, flat vibrant colors, {STYLE}"
    ),
}

# setting_en, footwear_en, a, b, c, d
EPISODES: dict[int, dict[str, str]] = {
    1: {
        "setting": "marzipane-roofed FrancaVilla with donut-shaped chimney smoke near a river bridge",
        "footwear": "giant brown leather boots",
        "a": f"{BASE}, {STYLE}, wearing giant brown leather boots, walking dusty path toward village market with empty party decoration basket, marzipane-roofed FrancaVilla, gentle THUMP dust clouds underfoot, morning Festa errand mood",
        "b": f"Desperate beaver Fred by crumbling dam on riverbank, water rushing toward squirrel tree-house, {BASE} arriving in background with brown leather giant boots, worried expression, {STYLE}, FrancaVilla riverside",
        "c": f"{BASE} standing in river as shield against current, trunk packing clay mud onto dam branches, covered head-to-toe in brown slime, ears shaking, FOCUS determined eyes, comic messy chaos, Fred watching amazed, {STYLE}",
        "d": f"Dried clay on {BASE} skin forming beautiful festive garland patterns, happy squirrels offering giant bundle of colorful ribbons and walnut sweets for village Festa, muddy elephant laughing, golden sunset, mission accomplished without supermarket, {STYLE}",
    },
    2: {
        "setting": "rocky mountain FrancaVilla with wild mint paths and misty blurred atmosphere",
        "footwear": "giant colorful lace-up walking shoes",
        "a": f"{BASE}, blurry soft world around him, wearing giant colorful walking shoes, squinting gently, walking toward owl optician across mint-scented rocky FrancaVilla, {STYLE}",
        "b": f"Tiny green gecko Jack crying in tall grass, lost dark sunglasses somewhere in meadow, {BASE} kneeling nearby in colorful giant shoes, gentle concern, {STYLE}, rocky FrancaVilla",
        "c": f"{BASE} lying on ground, trunk like vacuum cleaner over grass, eyes squinting hard in FOCUS, searching tiny objects, funny eye workout expression, Jack hopeful beside him, {STYLE}",
        "d": f"Tiny sunglasses perched on tip of elephant trunk, Jack cheering, {BASE} eyes wide and perfectly sharp clear world around, no optician needed, joyful surprise, {STYLE}",
    },
    3: {
        "setting": "golden rolling hills FrancaVilla with emerald meadows and sparkling streams",
        "footwear": "giant boots",
        "a": f"{BASE} in giant boots walking sunny main road of hilltop FrancaVilla, empty fruit basket, hungry hopeful expression, THUMP on golden path, afternoon snack mission, {STYLE}",
        "b": f"Giraffe Raffa with neck bent like broken umbrella, unable to reach village fountain, sad thirsty eyes, {BASE} approaching in giant boots, {STYLE}, golden hills FrancaVilla",
        "c": f"{BASE} spraying warm water massage from trunk onto giraffe stiff neck, steam mist, caring FOCUS face, Raffa surprised, fountain nearby, {STYLE}",
        "d": f"Giraffe neck straight and tall again, Raffa picking giant golden wild banana bunch from treetop for {BASE}, happy feast ready, {STYLE}, emerald meadow FrancaVilla",
    },
    4: {
        "setting": "tropical jungle-framed sunny FrancaVilla with jasmine-scented air",
        "footwear": "well-brushed giant boots",
        "a": f"{BASE} in polished giant boots marching to elephant dentist, touching rough left tusk thoughtfully, tropical FrancaVilla path, THUMP, {STYLE}",
        "b": f"Exhausted mouse Pino trying to dig burrow, hard rocks breaking tiny claws, old tree root, {BASE} with polished boots pausing on path, {STYLE}",
        "c": f"{BASE} tilting sideways using left tusk as pickaxe on hard rock, sparks and dust flying, FOCUS grit, Pino watching from hole entrance, {STYLE}, jungle FrancaVilla",
        "d": f"{BASE} left tusk gleaming like polished gold in river reflection, perfect burrow finished, Pino pointing excitedly, dentist unnecessary, {STYLE}",
    },
    5: {
        "setting": "white cobblestone artisan FrancaVilla with colorful toy-like shop fronts",
        "footwear": "giant rubber-sole shoes",
        "a": f"{BASE} carrying torn velvet jacket under arm, giant rubber-sole shoes on cobblestones, heading to tailor, THUMP, {STYLE}, artisan FrancaVilla",
        "b": f"Hedgehog Ciccio trapped in thorn bush, spines tangled in brambles, crying, {BASE} with torn jacket looking torn between errand and friend, {STYLE}",
        "c": f"{BASE} spreading beloved velvet jacket over thorns as shield, FOCUS ears flapping, Ciccio sliding out safe, jacket shredded to rags, comic sacrifice, {STYLE}",
        "d": f"Ciccio sewing colorful patchwork superhero cape for {BASE} using spines as needles, elephant wearing cape proudly, tailor errand forgotten happily, {STYLE}",
    },
    6: {
        "setting": "night FrancaVilla lit by silver river reflections and paper lanterns on balconies",
        "footwear": "giant soft wool slippers",
        "a": f"{BASE} in giant wool slippers at dusk, walking to bookstore before closing, paper lanterns glowing, quiet THUMP on fallen leaves, {STYLE}, night FrancaVilla",
        "b": f"Firefly Luce dim and feverish on dark forest path, lost without glow, {BASE} in wool slippers finding her, gentle worry, {STYLE}",
        "c": f"Tiny firefly riding on {BASE} head, elephant telling stories with expressive trunk, walking through dark woods, protective warm scene, FOCUS kindness, {STYLE}",
        "d": f"Hundreds of fireflies circling {BASE}, animated shadow stories projected on rocks like living picture book, no book purchase needed, magical night sky, {STYLE}",
    },
    7: {
        "setting": "red-brick industrial FrancaVilla with canals and clock towers",
        "footwear": "sturdy giant work boots",
        "a": f"{BASE} pushing giant bicycle with flat tires, sturdy work boots on brick road, heading to mechanic, THUMP, {STYLE}, industrial FrancaVilla",
        "b": f"Mole Ralph coughing at smoking underground hole, dry leaves burning in tunnel, gray smoke from ground, {BASE} with bike nearby, {STYLE}",
        "c": f"{BASE} standing over ventilation hole blowing enormous breath into tunnel, cheeks puffed, bicycle wobbling from shockwave, FOCUS heroic, {STYLE}",
        "d": f"Bicycle tires magically fully inflated from underground air pressure, Ralph safe waving, {BASE} ready to ride, comic physics victory, {STYLE}",
    },
    8: {
        "setting": "rural sunflower plain FrancaVilla with geometric irrigation canals",
        "footwear": "blue rubber giant boots",
        "a": f"Gray dusty {BASE} in blue rubber giant boots heading to elephant car wash, sunflower fields and tractors, THUMP on dirt road, {STYLE}",
        "b": f"Sad piglet Mino beside dried muddy puddle, sun beating down, risk of sunburn, farm near canal, {BASE} approaching, {STYLE}",
        "c": f"{BASE} spraying river water from trunk to recreate muddy puddle for piglet, getting even dustier himself, FOCUS helping, blue boots splashed, {STYLE}",
        "d": f"Perfect summer cloudburst shower over {BASE} like free car wash, Mino splashing happy in new puddle, rainbow light, {STYLE}, rural FrancaVilla",
    },
    9: {
        "setting": "snowy mountain FrancaVilla with pine forests and wooden chalet roofs",
        "footwear": "light giant boots",
        "a": f"{BASE} in light giant boots on mountain cobblestone, going to cobbler for winter boots, THUMP echo, {STYLE}, alpine FrancaVilla",
        "b": f"Caterpillar Bruno on leaf crying, forty-two tiny colorful shoes tied in one giant impossible knot, spring ball invitation, {STYLE}",
        "c": f"{BASE} trunk tip delicately untying microscopic shoelace knots with extreme FOCUS face, giant ears still, Bruno watching amazed, {STYLE}",
        "d": f"Bruno and friends doing rhythmic dance massage on {BASE} trunk like shoe polish spa, winter boots gleaming ready, {STYLE}, mountain village",
    },
    10: {
        "setting": "coastal FrancaVilla with salty alleys and golden beach fishing boats",
        "footwear": "red giant boots",
        "a": f"{BASE} in red giant boots carrying important letter to post office, sea breeze, THUMP on coastal path, {STYLE}",
        "b": f"Squirrel Renatolo under ancient oak, winter acorn stash fallen into deep narrow root crevice, desperate reach, {STYLE}, coastal FrancaVilla",
        "c": f"{BASE} trunk stuck in crevice like straw, cheeks full vacuuming acorns, one acorn jammed in trunk, comic bulging eyes, FOCUS strain, {STYLE}",
        "d": f"Giant sneeze launching acorn and letter flying perfectly toward post office window, Renatolo cheering, {STYLE}, oak tree coastal scene",
    },
    11: {
        "setting": "medieval FrancaVilla with stone bell towers and courtyard fountains",
        "footwear": "giant walking boots",
        "a": f"{BASE} in walking giant boots approaching old hospital for heart checkup, stone bell towers, calm morning THUMP, {STYLE}",
        "b": f"Little monkey Mietta clinging to chair terrified of nurse with syringe, hospital waiting room, {BASE} pausing kindly, {STYLE}",
        "c": f"{BASE} holding Mietta gently, flapping ears in silly games to distract from needle, FOCUS on friend not fear, warm comic hospital scene, {STYLE}",
        "d": f"Doctor listening to {BASE} laughing heart with stethoscope, strong healthy heartbeat visualized as golden glow, checkup complete, {STYLE}",
    },
    12: {
        "setting": "blue-tile rooftop FrancaVilla with hanging gardens and mural walls",
        "footwear": "giant walking boots",
        "a": f"{BASE} in walking boots heading to hardware store for lightbulb, blue tile rooftops and roses, THUMP, {STYLE}",
        "b": f"Sleepy owl Tufo with dark circles under tree, mischievous small birds singing loudly preventing sleep, {STYLE}, mural FrancaVilla square",
        "c": f"{BASE} sitting under tree spreading huge ears like umbrella over owl branch, FOCUS protective shadow, birds still chirping outside, {STYLE}",
        "d": f"Owl eyes glowing like living lightbulbs after rest, {BASE} holding burned-out bulb smiling, lamp unnecessary, warm evening glow, {STYLE}",
    },
    13: {
        "setting": "Nordic valley FrancaVilla with red firs, icy lakes and stone-heated floors",
        "footwear": "soft leather giant boots",
        "a": f"{BASE} in soft leather giant boots walking to bakery for ginger cookies, crisp Nordic air, THUMP on stone path, {STYLE}",
        "b": f"Bear Fosco with head stuck inside hollow beehive on branch, honey paws, panicked wiggle, {STYLE}, fir forest FrancaVilla",
        "c": f"{BASE} pulling beehive with trunk, FOSCO popping free but elephant covered in sticky honey from head to toe, comic sticky disaster, {STYLE}",
        "d": f"Golden pollen rain sticking to honey on {BASE} forming sparkling crown, bear grateful, cookie mission forgotten in magical shimmer, {STYLE}",
    },
    14: {
        "setting": "pastel hillside FrancaVilla with olive groves and ancient vineyards",
        "footwear": "giant boots",
        "a": f"{BASE} in giant boots going to nursery for daisy seeds, pastel facades and vines, THUMP, {STYLE}",
        "b": f"Butterfly Lalla with wing heavy from giant dew drop, unable to fly, curious cat creeping nearby, {STYLE}, flowered hills",
        "c": f"{BASE} flapping big ears like warm fans drying butterfly wing, FOCUS gentle breeze, cat kept at distance, {STYLE}",
        "d": f"Wild poppy and daisy seeds caught in elephant toe crevices, free garden seeds without nursery visit, Lalla flying circles happily, {STYLE}",
    },
    15: {
        "setting": "volcanic thermal FrancaVilla with gentle steam vents and dark rock gardens",
        "footwear": "giant boots",
        "a": f"{BASE} in giant boots walking to gelato shop, warm steam rising from ground, THUMP, volcanic FrancaVilla, {STYLE}",
        "b": f"Golden rescue dog Mayer sad, lost water bottle in dense thicket, hot day, {STYLE}, steamy garden path",
        "c": f"{BASE} retrieving bottle and blowing cool shaded forest air on panting dog, FOCUS care, still no gelato yet, {STYLE}",
        "d": f"Mayer sharing frozen coconut milk and wild berries from special bottle with {BASE}, better than gelato cone, happy cool feast, {STYLE}",
    },
    16: {
        "setting": "stilt-house river FrancaVilla with rope bridges and colorful boats below",
        "footwear": "giant boots",
        "a": f"{BASE} in giant boots heading to newsstand for Super-Elephant comic, wooden stilt walkways, THUMP, {STYLE}",
        "b": f"Cold monkey Betta shivering, scarf stuck on highest jungle branch above river, {STYLE}, stilt FrancaVilla",
        "c": f"{BASE} standing on hind legs stretching trunk upward, FOCUS strain reaching scarf, wobble comic balance, {STYLE}",
        "d": f"Betta throws old colorful newspaper page from branch — rare first-edition Super-Elephant comic cover art, better than newsstand, {STYLE}",
    },
    17: {
        "setting": "woodworking FrancaVilla with carpenter shops and swinging tavern signs",
        "footwear": "giant work boots",
        "a": f"{BASE} in work boots carrying wobbly wooden chair to carpenter, THUMP on workshop street, {STYLE}",
        "b": f"Lively mouse Lendo trapped under fallen heavy tavern sign he accidentally unscrewed, panic, {STYLE}, carpenter quarter",
        "c": f"{BASE} holding massive sign steady against wall with immense strength, FOCUS muscles, Lendo scrambling out, {STYLE}",
        "d": f"Lendo carving perfect wooden wedge with sharp teeth fixing chair leg instantly, chair stable, {STYLE}, warm workshop glow",
    },
    18: {
        "setting": "canal FrancaVilla with flower bridges and lavender-scented windmills",
        "footwear": "giant boots splashed with paint",
        "a": f"{BASE} in paint-splashed giant boots going to paint shop for sky-blue fence paint, canals and windmills, {STYLE}",
        "b": f"Sad unicorn Morno in morning fog, rainbow mane turned dull gray, magical creature lost sparkle, {STYLE}",
        "c": f"{BASE} gently rubbing unicorn coat with soft trunk tip, FOCUS friendship warmth, fog swirling, {STYLE}",
        "d": f"Unicorn horn shooting rainbow beam that paints fence and sky perfectly blue, paint can unnecessary, magical joy, {STYLE}",
    },
    19: {
        "setting": "fairy-tale clearing FrancaVilla with pink pebble paths and neat blueberry hedges",
        "footwear": "bright green rubber giant boots",
        "a": f"{BASE} in bright green rubber boots walking to greengrocer for lettuce, pink pebble paths, THUMP, {STYLE}",
        "b": f"Turtle Lattuga with plastic bucket stuck on shell, cannot walk, desperate on nettle path, {STYLE}",
        "c": f"{BASE} shaking turtle gently to free bucket, bucket flies spinning through air, comic chaos, FOCUS effort, {STYLE}",
        "d": f"Flying bucket hits wild tree dropping basket of perfect lettuce and vegetables for elephant, turtle free smiling, {STYLE}",
    },
    20: {
        "setting": "majestic FrancaVilla with stone statues, lavender fountains and royal palace gardens",
        "footwear": "formal giant boots",
        "a": f"{BASE} in formal giant boots carrying cane sugar package to Royal Palace kitchens, statues and fountains, THUMP, {STYLE}",
        "b": f"Queen bee Regina lying bloated on palace garden path, indigestion after feast, worried hive, {STYLE}",
        "c": f"{BASE} holding queen bee on trunk doing slow gentle walking wiggle exercise, FOCUS care, sugar package slipping, {STYLE}",
        "d": f"Spilled sugar attracting royal bees who weave golden honey gift crown for {BASE}, palace delivery complete magically, {STYLE}",
    },
    21: {
        "setting": "pastel mountain-foot FrancaVilla with tall bell tower piercing cream-cloud sky",
        "footwear": "giant walking boots",
        "a": f"{BASE} in walking boots buying morning newspaper at hilltop kiosk, pastel houses, THUMP, {STYLE}",
        "b": f"Unicorn butterfly Lalla with tiny horn stuck on low cloud near bell tower top, vertigo fear, misty height, {STYLE}",
        "c": f"{BASE} on narrow bell tower external stairs reaching trunk toward butterfly, hat blown off, balancing FOCUS, windy comic peril, {STYLE}",
        "d": f"Butterfly landing on trunk, village below looking like tiny LEGO toys, fear conquered, newspaper headline already known from view, {STYLE}",
    },
    22: {
        "setting": "agricultural checkerboard FrancaVilla with vegetable rows and lazy windmills",
        "footwear": "green rubber giant boots",
        "a": f"{BASE} in green rubber giant boots with woven basket walking white farm path, cabbage fields and windmills, spring THUMP dust, {STYLE}",
        "b": f"Gray rabbit Otto with only ears sticking out of mud mound, collapsed burrow entrance after rain, tears, {STYLE}, farm field",
        "c": f"{BASE} kneeling digging with trunk, mud avalanche burying rabbit to ears and soaking elephant to knees, FOCUS gone wrong, path blocked, {STYLE}",
        "d": f"Ancient terracotta drain pipe cleared, water flowing to ditch, giant carrots and celery sprouting, farmer filling basket for {BASE}, repaired burrow, {STYLE}",
    },
    23: {
        "setting": "flowery FrancaVilla community garden with lavender rows, geranium balconies and jasmine avenue",
        "footwear": "giant white Sunday slippers",
        "a": f"{BASE} in giant white Sunday slippers carrying wicker basket and empty honey jar, walking jasmine-scented path to community garden, soft THUMP, evening tea errand mood, {STYLE}",
        "b": f"Kind little girl Iris with braids and floral apron crying beside broken tin watering can, wilting daisy seedlings in pots, {BASE} approaching gently in white slippers, {STYLE}, flower garden FrancaVilla",
        "c": f"{BASE} spraying water delicately from trunk onto flower pots, too much spray creating muddy stream on path, white slippers covered in mud, empty jar rolling, FOCUS caring chaos, {STYLE}",
        "d": f"Bees escorting {BASE} along dry clover path, beekeeper filling two golden honey jars, Iris tying yellow ribbon on jar, star-shaped honeycomb slice, saved flowers blooming, {STYLE}",
    },
    24: {
        "setting": "woodland FrancaVilla among pine hills with resin-scented misty morning paths",
        "footwear": "giant brown forest hiking boots",
        "a": f"{BASE} in giant brown forest boots carrying wicker basket, walking pine needle path toward carpenter workshop, THUMP shaking mushrooms, shelf bracket errand, {STYLE}",
        "b": f"Badger Rufus with white-black snout scratching desperately at fallen log blocking burrow entrance, tiny grunts from inside, worried eyes, {STYLE}, pine forest FrancaVilla",
        "c": f"{BASE} pushing huge round log which rolls downhill like barrel, elephant chasing, bent metal bracket flying from basket, comic forest chase, FOCUS, {STYLE}",
        "d": f"Log plugging leaky rain barrel perfectly, carpenter offering new ornate iron bracket with oak leaf engraving, baby badgers hugging Rufus, dried red apples in basket for {BASE}, {STYLE}",
    },
    25: {
        "setting": "stilt-house maritime FrancaVilla lagoon with wooden walkways and floating mill",
        "footwear": "giant yellow fisherman boots",
        "a": f"{BASE} in giant yellow fisherman boots carrying heavy rice sack on back, walking creaking wooden pier toward floating windmill, THUMP, morning mist, {STYLE}",
        "b": f"Elegant gray crane Esau with one leg tangled in abandoned fishing net on pier, wings flapping in wind, frightened dark eyes, {BASE} approaching carefully in yellow boots, {STYLE}, lagoon FrancaVilla",
        "c": f"{BASE} wrapped in snapped-back fishing net around tusks and legs, rice sack burst scattering white grains on pier, crane watching, comic bind, FOCUS patience gone wrong, {STYLE}",
        "d": f"Free crane doing graceful dance gathering rice grains into neat pile with wing breeze, miller offering fresh flour sack from floating mill, sunset over lagoon, season 1 finale mood, {STYLE}",
    },
    26: {
        "setting": "bakery FrancaVilla with wheat-roof chimneys, wood-fired oven steam and cobblestone flour path",
        "footwear": "giant cinnamon anti-slip baker slippers",
        "a": f"{BASE} in giant cinnamon baker slippers carrying clean tea towel, walking toward wood-fired bakery at morning, warm bread steam, THUMP on cobblestones, {STYLE}",
        "b": f"Red fox Nora with flour-covered muzzle, broken flour sack on sidewalk, slippery white street, {BASE} approaching in cinnamon slippers, worried fox, {STYLE}, bakery village",
        "c": f"{BASE} covered head-to-toe in white flour cloud after sweeping with trunk, sneezing, windows and pavement dusted white, comic powder chaos, FOCUS, {STYLE}",
        "d": f"Warm oven breeze creating perfect golden crust on loaves, baker filling basket with hot bread for {BASE}, new flour sack with orange ribbon for fox Nora, {STYLE}",
    },
    27: {
        "setting": "riverside FrancaVilla with pale stone houses, creaking wooden bridges and sweet dairy steam from cheese shop",
        "footwear": "giant moss-green waterproof shoes",
        "a": f"{BASE} in giant moss-green waterproof shoes carrying wicker basket, walking river path toward cheese shop at noon, white dairy steam, THUMP on wooden bridge planks, {STYLE}",
        "b": f"Agile caring otter Leda beside two milk buckets on riverbank, moss-covered slippery wooden slide to dairy, frightened eyes, {BASE} approaching in green shoes, {STYLE}, riverside FrancaVilla",
        "c": f"{BASE} covered in green plane-tree leaf avalanche after scattering too many leaves on mossy path, leaf hat on head, FOCUS ears shaking, comic forest carpet chaos, otter watching, {STYLE}",
        "d": f"Compacted wet leaves forming natural bridge over stream, dairy Gina gifting fresh white mozzarella in basket for {BASE} and orange-handle bucket for otter Leda, {STYLE}",
    },
    28: {
        "setting": "circus-week FrancaVilla with red-yellow striped tents, tightropes between lampposts and cotton-candy air",
        "footwear": "giant colorful polka-dot party slippers",
        "a": f"{BASE} in giant colorful polka-dot party slippers walking excitedly toward circus ticket booth in village square, festive banners, THUMP on cobblestones, {STYLE}",
        "b": f"Deflated flat red balloon Pippo with painted smile lying sadly on grass, lost air after wind, {BASE} kneeling nearby in polka-dot slippers, gentle concern, {STYLE}, circus FrancaVilla",
        "c": f"{BASE} red-faced puffing too hard into balloon valve, black hair tuft standing straight up, balloon Pippo zigzagging wildly between lampposts, comic breath chaos, FOCUS, {STYLE}",
        "d": f"Popcorn machine warm air perfectly inflating round red balloon Pippo, golden first-row ticket landing on elephant trunk, circus director cat applauding, {STYLE}",
    },
    29: {
        "setting": "hillside FrancaVilla with terraced houses climbing toward observatory dome and oil-lamp evening glow",
        "footwear": "giant soft night-blue silent boots",
        "a": f"{BASE} in giant soft night-blue boots climbing hill path at dusk carrying canvas sack, indigo sky, quiet THUMP, night-lamp shop errand, {STYLE}",
        "b": f"Wise owl astronomer Otis on perch with torn star-map paper fragments, worried golden eyes, children path below in dark, {BASE} arriving in night-blue boots, {STYLE}, observatory FrancaVilla",
        "c": f"{BASE} trunk raised reflecting twilight like beacon, golden dusty moth powder covering elephant head-to-toe sparkling, FOCUS guiding light, comic glitter chaos, {STYLE}",
        "d": f"Moths tracing glowing golden Swan constellation on white observatory wall, children marveling, real stars above through opened dome, no lamp needed, {STYLE}",
    },
    30: {
        "setting": "seamstress FrancaVilla with colorful thread shop windows, fabric-scented sidewalks and underground tailor tunnels",
        "footwear": "giant soft gray wool shoes",
        "a": f"{BASE} in giant soft gray wool shoes carrying torn wind-cloak fabric piece, walking toward underground haberdashery, morning THUMP, {STYLE}, tailor village",
        "b": f"Timid mole seamstress Tina with checkered apron beside dark hole, reversed buttons and pins mixed with sand, glasses on head, {BASE} approaching in gray wool shoes, {STYLE}",
        "c": f"{BASE} trunk pulling buttons pins and yarn balls into colorful tornado on floor, blue button stuck in elephant ear, FOCUS sorting chaos, comic sewing mess, {STYLE}",
        "d": f"Small earth tremor revealing hidden golden star-shaped buttons in sand, Tina sewing stars on festival dress, blue thread mended wind-cloak for {BASE}, {STYLE}",
    },
    31: {
        "setting": "citrus FrancaVilla with white garden walls, yellow lemon pergolas and sweet zagara blossom scent",
        "footwear": "giant bright lemon-yellow slippers",
        "a": f"{BASE} in giant bright lemon-yellow slippers carrying large harvest basket through sunny lemon grove, yellow tunnel of leaves, THUMP, {STYLE}",
        "b": f"Shy chameleon Ciro camouflaged on lemon with gentle blinking eyes, mother searching hours, afraid to move, {BASE} in yellow slippers pausing, {STYLE}, citrus FrancaVilla",
        "c": f"{BASE} giant sneeze shaking lemon grove, yellow lemons raining and rolling everywhere, chameleon Ciro turning bright green on branch, leaf on elephant head, FOCUS, {STYLE}",
        "d": f"Rolled lemons landing perfectly in farmer market cart, fresh lemonade with ice and mint for all, chameleon reunited with mother, {STYLE}",
    },
    32: {
        "setting": "summer FrancaVilla with communal azure pool, plastic palm gate decorations and light chlorine scent",
        "footwear": "worn giant old flip-flops",
        "a": f"{BASE} in worn giant old flip-flops squish-squashing toward sports shop beside community pool, sunny morning THUMP, {STYLE}",
        "b": f"Timid fluffy yellow duckling Dodo circling in shallow kiddie pool, slippery edge fear, mother ducks calling outside, {BASE} with old flip-flops nearby, {STYLE}, pool FrancaVilla",
        "c": f"{BASE} gentle trunk shower becoming too generous, flooded pool vestibule with rainbow mirror reflections, water drop on hair tuft, FOCUS helping, comic splash chaos, {STYLE}",
        "d": f"Warm water clearing clogged drain, brave duckling Dodo reunited with mother, new blue-orange anti-slip sandals floating on tray to elephant feet, {STYLE}",
    },
    33: {
        "setting": "epistolary FrancaVilla with brass post-office bell, colorful postcard windows and damp morning square",
        "footwear": "giant elegant burgundy shoes",
        "a": f"{BASE} in giant elegant burgundy shoes carrying carefully written letter envelope, walking to philately shop, THUMP on square stones, {STYLE}",
        "b": f"Diligent tired hedgehog postman Elio beside humidity-stuck pile of envelopes, stamps at risk, spines lowered from stress, {BASE} in burgundy shoes approaching, {STYLE}",
        "c": f"{BASE} carefully separating envelopes with trunk when sudden wind scatters colorful stamps like paper butterflies across square, chasing stamps comic chaos, FOCUS, {STYLE}",
        "d": f"Stamps landing on pavement forming perfect red-green-blue heart shape, head postmistress owl gifting special golden stamp for aunt letter, community smiling, {STYLE}",
    },
    34: {
        "setting": "musical FrancaVilla with cedar-scented violin workshops, wind chimes on every balcony and quiet garden paths",
        "footwear": "giant mahogany-colored boots",
        "a": f"{BASE} in giant mahogany boots carrying broken silent wind-chime, walking breezy path to luthier workshop, THUMP, {STYLE}",
        "b": f"Elegant red fox musician Viola with purple bow in ear, violin bow stuck in thorny hedge before concert, frustrated eyes, {BASE} in mahogany boots nearby, {STYLE}",
        "c": f"{BASE} bending hedge branches gently then sudden green leaf rain covering street rooftops and luthier hat, leaf on trunk tip, FOCUS patience, {STYLE}",
        "d": f"Fallen leaves vibrating on cobblestones like harp strings guiding to hidden bow, repaired wind-chime for {BASE}, spare strings gifted to Viola, {STYLE}",
    },
    35: {
        "setting": "Sunday market FrancaVilla with colorful vegetable stalls, bread scent and cheerful farmer calls",
        "footwear": "giant sturdy market shoes with thick soles",
        "a": f"{BASE} in giant sturdy market shoes carrying empty jute sack toward vegetable market on Sunday morning, lively THUMP, {STYLE}",
        "b": f"Golden-cheeked hamster Patata pushing stuck cart wheel trapped in cobblestone pothole, potatoes for village soup, {BASE} approaching in market shoes, {STYLE}",
        "c": f"{BASE} pushing cart too hard, wheel detaching and rolling downhill like mad circle, elephant frozen mid-street comic pause, FOCUS, {STYLE}",
        "d": f"Runaway wheel plugging deep pothole perfectly, striped-apron capybara merchant filling sack with round potatoes for {BASE}, new cart plank for hamster Patata, {STYLE}",
    },
    36: {
        "setting": "after-storm FrancaVilla with sky-reflecting puddles, washed alleys and fresh clean air",
        "footwear": "giant anti-slip rain slippers",
        "a": f"{BASE} in giant anti-slip rain slippers carrying folded broken umbrella toward repair shop, wet cobblestones, THUMP through puddles, {STYLE}",
        "b": f"Small rainbow-colored lizard Iris Arcobaleno slipping on glass-smooth stone stairs, tana reflected on wall above, {BASE} with large drying cloth, {STYLE}",
        "c": f"{BASE} drying stairs while puddle reflections paint luminous rainbow patches on trunk legs and black hair tuft, walking rainbow elephant, FOCUS, {STYLE}",
        "d": f"Sunlit droplets on hair tuft creating perfect mini-rainbow bridge to wall tana, repaired umbrella returned free but sky clear, children applauding from windows, {STYLE}",
    },
    37: {
        "setting": "summer FrancaVilla with gray stone icehouse in square, cold morning mist and glittering ice blocks",
        "footwear": "giant summer shoes",
        "a": f"{BASE} in giant summer shoes carrying insulated bucket toward icehouse on hot afternoon, shimmering heat, THUMP on square stones, {STYLE}",
        "b": f"Curious traveling penguin Ping with striped scarf sliding helplessly on ice block glued to pavement, small backpack, {BASE} approaching, {STYLE}, icehouse FrancaVilla",
        "c": f"{BASE} gentle warm breath loosening ice then slipping on mirrored ice rink pavement, legs in air comic skating pose, FOCUS welcoming, {STYLE}",
        "d": f"Ice block sculpted into small elephant monument, icehouse keeper filling bucket with cubes and two fresh fruit smoothies for {BASE} and penguin Ping, {STYLE}",
    },
    38: {
        "setting": "green terrace FrancaVilla with potted plants on external stairs climbing to rooftop nursery",
        "footwear": "giant garden clogs with clean soles",
        "a": f"{BASE} in giant garden clogs climbing external stairs toward rooftop nursery for basil pot, earthy morning THUMP, {STYLE}",
        "b": f"Caring marmot gardener Mirta in green apron beside dangerously tilting flower box over sidewalk, tunnel under heavy pot, {BASE} steadying below in garden clogs, {STYLE}",
        "c": f"{BASE} holding heavy basil pot steady with trunk while dark fertile soil falls to sidewalk below forming brown mound, FOCUS column pose, {STYLE}",
        "d": f"Soil mound filling sidewalk pothole for sparrow nest, doubled-leaf basil pot plus second gifted pot from straw-hat nursery otter, safe flower box, {STYLE}",
    },
    39: {
        "setting": "vanilla-scented pastry FrancaVilla with sugar-roof houses, buttery shop windows and croissant morning air",
        "footwear": "giant cream-white anti-slip chef shoes",
        "a": f"{BASE} in giant cream-white chef shoes carrying paper sack toward pastry shop for Grande Festa streamers and ribbons, golden morning THUMP, {STYLE}",
        "b": f"Experienced beaver Bruno in flour apron beside broken mini dam flooding bakery channel near mixer, panicked splash, {BASE} in cream chef shoes arriving, {STYLE}",
        "c": f"{BASE} packing leak with twigs and mud too zealously, sugary water flooding white bakery floor around elephant feet like glaze slippers, FOCUS, {STYLE}",
        "d": f"Oven steam meeting humidity creating fragrant mist puffing perfect golden pastries, baker Clara gifting colorful streamers ribbons and pastry box to {BASE} and beaver Bruno, {STYLE}",
    },
    40: {
        "setting": "windy hilltop FrancaVilla with spiral snail-shell paths, pointed roofs touching low clouds and thyme evening scent",
        "footwear": "giant cloud-tread hiking boots",
        "a": f"{BASE} in giant cloud-tread hiking boots carrying wrapped binoculars up hillside path before dark, windy THUMP, {STYLE}",
        "b": f"Young brave owl Stella beside overturned wicker basket with three pale cold eggs on rosemary bush, father searching branch, {BASE} setting binoculars down gently, {STYLE}",
        "c": f"{BASE} standing still with huge ears draped over egg basket like warm blankets, sleepy swaying almost falling, FOCUS protective silence, {STYLE}",
        "d": f"Orange sunset warmth under ears, father owl rebuilding nest on safe low branch, fallen binoculars pointing perfectly at reunited eggs, astronomer bear applauding, {STYLE}",
    },
    41: {
        "setting": "red-brick railway FrancaVilla with steam clouds over shiny tracks and creaking wooden platform signs",
        "footwear": "giant brown traveler boots with shiny buckle",
        "a": f"{BASE} in giant brown traveler boots with shiny buckle carrying travel bag toward small station ticket office, afternoon THUMP on platform, {STYLE}",
        "b": f"Determined badger railwayman Treno in oversized stationmaster cap beside fallen red signal on tracks, blank departure board, {BASE} approaching, {STYLE}",
        "c": f"{BASE} lifting heavy red signal with trunk accidentally pulling test whistle cord, deafening FIEEEE sound, travelers jumping, comic shockwave, FOCUS, {STYLE}",
        "d": f"Signal shadow revealing loose rail and bent nail underneath, workers repairing track, golden ticket handed free to {BASE}, safe departure board lit, {STYLE}",
    },
    42: {
        "setting": "mossy forest-edge FrancaVilla with mushroom umbrellas under ferns, pine scent and misty brook songs",
        "footwear": "giant green forest boots with leaf-tread soles",
        "a": f"{BASE} in giant green forest boots with leaf tread carrying old crooked wicker basket toward forest basket-maker, soft earth THUMP, {STYLE}",
        "b": f"Calm round capybara Fungo sitting on flooded mossy bank, submerged slippery log bridge over brook, aromatic herbs needed across stream, {STYLE}",
        "c": f"{BASE} stepping on floating logs which sink under weight spraying gentle mud on capybara muzzle and black hair tuft, FOCUS careful steps, {STYLE}",
        "d": f"Green algae pads floating under logs as natural cushions, forest animals crossing safely, basket-maker gifting new waterproof willow basket to {BASE}, {STYLE}",
    },
    43: {
        "setting": "lively FrancaVilla town square with hand-painted shop signs, dripping fountain and fresh printer's ink smell",
        "footwear": "giant pastel-splattered artist slippers",
        "a": f"{BASE} in giant pastel-splattered artist slippers carrying folder toward typography shop for Festa posters, sunny square THUMP, {STYLE}",
        "b": f"Magnificent peacock Pennello with tail feathers stuck in bucket of fresh paint preparing Festa banners, distressed creative eyes, {STYLE}",
        "c": f"{BASE} stirring paint with trunk too enthusiastically, red yellow blue arcs splashing cobblestones fountain base and typography stairs, FOCUS, {STYLE}",
        "d": f"Paint splatters on square forming giant smiling elephant mural seen from bell tower, iridescent peacock-feather posters gifted free, children dancing on colors, {STYLE}",
    },
    44: {
        "setting": "seaside FrancaVilla with pearlescent shells on sand, salty wooden boardwalk and gentle wave lines",
        "footwear": "giant yellow wave-pattern beach boots",
        "a": f"{BASE} in giant yellow wave-pattern beach boots carrying sack toward seaside shop for Festa volleyball net, breezy boardwalk THUMP, {STYLE}",
        "b": f"Gentle dark-shelled sea turtle Sabrina carefully moving stones on beach, erased nest markers after tide, worried salt tears, {STYLE}, maritime FrancaVilla",
        "c": f"{BASE} drawing enormous confusing arrow-and-circle labyrinth in sand with giant foot, turtle Sabrina pointing to real nest location, comic map chaos, FOCUS, {STYLE}",
        "d": f"Beach volunteers forming ribbon cordon around true nest dune, shopkeeper gifting lightweight net for Festa games to {BASE}, star-marked shell beside nest, {STYLE}",
    },
    45: {
        "setting": "stone communal washhouse FrancaVilla with flowing troughs, sun-dried linens and Marseilles soap scent",
        "footwear": "giant blue florist boots with white polka-dot soles",
        "a": f"{BASE} in giant blue polka-dot sole boots carrying empty basket toward washhouse market for Marseilles soap, wet stones THUMP, {STYLE}",
        "b": f"Lively bright green frog Rina leaping between washtubs, soap bubbles making floor dangerously slippery, friends falling with laundry cages, {STYLE}",
        "c": f"{BASE} collecting bubbles with trunk then sitting splash in wet tablecloths and foam hat on hair tuft, everyone laughing together, FOCUS balance lost, {STYLE}",
        "d": f"Remaining bubbles floating to market facade reflecting perfect rainbow, soap-seller gifting fragrant soap bar and pre-ironed Festa linens to {BASE}, {STYLE}",
    },
    46: {
        "setting": "golden agricultural FrancaVilla with sunflower fields, creaking hay carts and warm cut-grass air",
        "footwear": "giant brown farmer boots with plow-line soles",
        "a": f"{BASE} in giant brown farmer boots carrying small spade toward seed nursery across windy golden fields, THUMP between rows, {STYLE}",
        "b": f"Stubborn gray donkey Girasole with pale mane pulling hay cart stuck in deep field rut, hungry lambs waiting at fence, {STYLE}",
        "c": f"{BASE} pulling cart with trunk too sharply, golden hay flying like snow over entire field covering freshly scattered seeds, FOCUS listening to donkey, {STYLE}",
        "d": f"Hay blanket holding wind-blown seeds in perfect even planting, seed nursery gifting extra packet of sunflowers daisies and lavender for Festa flower bed to {BASE}, {STYLE}",
    },
    47: {
        "setting": "festive shop FrancaVilla with ribbon-filled windows, stacked packages and freshly cut wrapping-paper scent",
        "footwear": "giant red festive boots with shiny toe caps",
        "a": f"{BASE} in giant red festive boots carrying gift list toward wrapping shop before Grande Festa, hurried afternoon THUMP, {STYLE}",
        "b": f"Precise little hedgehog Regalo tangled in infinite knot of colorful ribbons and bows blocking shop exit, teary spines, {STYLE}",
        "c": f"{BASE} trunk tip untying knots until elastic ribbon BOING wraps shelves chandelier and elephant trunk in rainbow yarn ball, FOCUS, {STYLE}",
        "d": f"Stretched ribbon from door to window forming giant visible bow attracting plaza crowd, shopkeeper gifting wrapping paper rolls and pre-wrapped Festa packages to {BASE}, {STYLE}",
    },
    48: {
        "setting": "white windmill FrancaVilla on hill with slow water wheel, grain sacks and fresh flour in summer breeze",
        "footwear": "giant beige miller boots with wheat-ear tread soles",
        "a": f"{BASE} in giant beige miller boots carrying cloth toward hilltop mill for whole-wheat flour sack before evening shutdown, wooden bridge THUMP, {STYLE}",
        "b": f"Electric-blue butterfly Vento with wings caught in grain-drying net beside mill path, trembling antennae, urgent message for miller, {STYLE}",
        "c": f"{BASE} carefully cutting net with wooden knife in trunk, flour sack bursting into soft white snow covering path and black hair tuft, sneezing ETCHEW, FOCUS, {STYLE}",
        "d": f"Gentle mill breeze guiding spilled flour through wooden chute to correct storehouse, free whole-wheat sack and warm test cake for {BASE}, butterfly Vento flying free, {STYLE}",
    },
    49: {
        "setting": "marzipane Festa-ready FrancaVilla with gingerbread chimneys puffing star-shaped smoke and anticipation in every lane",
        "footwear": "giant polished brown leather boots",
        "a": f"{BASE} in giant polished brown leather boots carrying spare confetti sack toward friend Franca yellow house to prepare Grande Festa, THUMP on dirt road, {STYLE}",
        "b": f"Beloved friend Franca with hair up and polka-dot apron beside wobbling too-small table covered in plates cups and ribbon rolls, {BASE} steadying table with trunk, {STYLE}",
        "c": f"{BASE} holding table while window gust WHOOOSH scatters confetti ribbons and paper across room sticking to chandelier cat and hair tuft, FOCUS, {STYLE}",
        "d": f"Season one and two animal friends arriving with banners pastries and extra cups, Franca house becoming warm heart of Grande Festa preparation, united joy, {STYLE}",
    },
    50: {
        "setting": "lantern-filled Grande Festa FrancaVilla square blending marzipane rooftops, mill hill, beach flags and forest garlands",
        "footwear": "giant golden star-tread Festa boots",
        "a": f"{BASE} in giant golden star-tread Festa boots carrying ladder gentle hammer and confetti sack toward central plaza before bell rings, joyful THUMP shaking banners, {STYLE}",
        "b": f"All beloved friends gathered in decorated square, Franca Bruno Nora Renatolo Jack Raffa Mietta Leda Otis Iris and many others, missing central festoon, sky waiting, {STYLE}",
        "c": f"{BASE} running ladder to stage and back, confetti pouring from boots, festoons tangling into colorful embrace around central stage, comic preparation chaos, FOCUS, {STYLE}",
        "d": f"Sweet scented cinnamon-honey sugar-firework confetti rain from gentle butterfly breeze, central garland blooming open above {BASE}, whole FrancaVilla family hugging, season 2 finale joy, {STYLE}",
    },
}
