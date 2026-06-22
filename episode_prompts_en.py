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
        "a": f"{BASE}, {STYLE}, wearing giant brown leather boots, walking dusty path toward village market with empty gift basket, marzipane-roofed FrancaVilla, gentle THUMP dust clouds underfoot, morning errand mood",
        "b": f"Desperate beaver Fred by crumbling dam on riverbank, water rushing toward squirrel tree-house, {BASE} arriving in background with brown leather giant boots, worried expression, {STYLE}, FrancaVilla riverside",
        "c": f"{BASE} standing in river as shield against current, trunk packing clay mud onto dam branches, covered head-to-toe in brown slime, ears shaking, FOCUS determined eyes, comic messy chaos, Fred watching amazed, {STYLE}",
        "d": f"Dried clay on {BASE} skin forming beautiful cake-icing patterns, happy squirrels offering giant walnut cake on tray, muddy elephant laughing, golden sunset, mission accomplished without supermarket, {STYLE}",
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
}
