# Python-p

Python-Project
Vážení nadšenci do programování v jazyce Python. Tímto bych Vám rád představil svůj projekt.

Projekt využívá knihovnu request a BeautifulSoup, která slouží k získávání dat z webových stránek. Dále knihovny time a datetime, které umí získat aktuální čas. Také pracuje s databází Mysql workbench.

Při startu program začne shromažďovat html adresy všech grafických karet na eshopu czc.cz a softcom.cz. Poté projde každou z těchto adres zvlášť a stáhne informace o kódu výrobce, ceně, ceně bez DPH a názvu všech těhto grafických karet. Dále zjistí, jestli tyto dva eshopy prodávají totožnou grafickou kartu. Pokud ano, smrskne informace o této kratě z obou eshopů dohromady a předbytečné(opakující se) vymaže. V neposlední řadě přemění data na vhodný formát a spolu s aktuálním časem je uloží do mysql workbench databáze, kde má každý řádek svůj jedinečný identifikátor v podobě čísla. Celý tento proces získávání a ukládání dat se opakuje každých pět minut.

Návrhy na vylepšění:

Přidat více eshopů. Urychlit proces. Omezit počet otevření webových stránek za jednotku času. Uplatnit koncept na jiná data než data grafických karet.
Při opakovaném spuštění programu by se již dříve zapsané výrobky neukládali do databáze jako nové, aby netvořili duplikáty. Místo toho se z nových dat vezme cena, ale pouze v případě, že se od minulého zápisu změnila. Každý produkt bude mít svojí vlastní tabulku, ve které budou zapsány průběžné změny cen spolu s časem zápisu pro každý z prohledávaných eshopů. Obě tabulky, jak s produkty, tak tabulky jednotlivých produktů s cenami budou obsahovat totožné kódy výrobků pro snažší orientaci.


