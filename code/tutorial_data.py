house_dict = {
    'cadon': 'Bearers of the Mark of Making, the artificers of House Cadon are responsible for creating the Forgelings, Zephyr, and the airships.',
    'donric': 'House Donric is made up of soldiers and bodyguards with the Mark of Sentinel, and its Blade Guild is the only standing army in Caeros.',
    'ghammara': 'Those with the Mark of Hospitality license inns and restaurants throughout Caeros and operate enclaves that offer sanctuary to fugitives and refugees.',
    'jeordo': 'The medics of House Jeordo use the Mark of Healing to mend bones and cure diseases -- for those that can afford it.',
    'kjaldar':'The banker of choice for the wealthy and powerful, House Kjaldar uses the Mark of Warding to guard strongholds and vaults containing great wealth.',
    'larenthil':'The Larenthils are masters of sea and sky, using the Mark of Storm to control the weather and operate elemental airships.',
    'micaeli':'Nothing escapes the notice of House Micaeli, whose members bear the Mark of Detection and are master investigators, researchers, and spy catchers.',
    'oraite':'Oraite carries the Mark of Passage and dominate the business of travel, operating the massive magical train called Zephyr which travels across Caeros.',
    'phaelanmyr':'Those of House Phaelanmyr bear the Mark of Shadow, and carry two faces: they are the house of entertainment, music, and art, and the house of spies and secrecy.',
    'saryn':'Bearing the Mark of Scribing, the Saryns are masters of the written word, working as mediators, translators, and mediators of the law.',
    'thagash':'The youngest house, Thagash consists of reckless prospectors and bounty hunters who use the Mark of Finding to locate deposits of Eldershards and dangerous criminals alike.',
    'vernalis':'Those of House Vernalis bear the Mark of Handling, which gives them a bond to natural creatures; their main business is breeding magical and ordinary animals.'
    }
    
def house_info(house):
    try:
        return house_dict[house.lower()]
    except:
        print "The house you entered was not recognized."
        return