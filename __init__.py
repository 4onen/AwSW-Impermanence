from modloader.modclass import Mod, loadable_mod

import jz_magmalink as ml

import renpy

def no_reenlightenment():
    skip_condition = '(persistent.endingsseen > 0 and trueselectable == False) or (persistent.impermanence_four_no_reenlightenment == True and persistent.trueending == True)'
    args = {'condition':skip_condition,'return_link':False}
    ( ml.find_label('seccont')
        .search_scene('chap1')
        .search_with()
        .hook_to('impermanence_four_no_reenlightenment_c1',**args)
        .search_python('renpy.pause(4.0)')
        .link_from('impermanence_four_no_reenlightenment_c1_end')
    )

    ( ml.find_label('chapter2')
        .search_scene('chap2')
        .search_with()
        .hook_to('impermanence_four_no_reenlightenment_c2',**args)
        .search_python('renpy.pause(2.0)')
        .link_from('impermanence_four_no_reenlightenment_c2_end')
    )

    c3 = ml.find_label('chapter3').search_scene('chap3').search_with()
    ( c3.search_if('carddisplayed == False')
        .link_from('impermanence_four_no_reenlightenment_c3_end')
    )
    c3.hook_to('impermanence_four_no_reenlightenment_c3_end',**args)

    c4 = ml.find_label('chapter4').search_python('carddisplayed = False')
    ( c4.search_if('carddisplayed == False')
        .link_from('impermanence_four_no_reenlightenment_c4_end')
    )
    c4.hook_to('impermanence_four_no_reenlightenment_c4_end',**args)
    

    c5 = ml.find_label('chapter5').search_python('carddisplayed = False')
    ( c5.search_if('carddisplayed == False')
        .link_from('impermanence_four_no_reenlightenment_c5_end')
    )
    c5.hook_to('impermanence_four_no_reenlightenment_c5_end',**args)


def testresults():
    testresultsif = ml.find_label('c4skip1') \
        .search_if('persistent.endingsseen > 0') \
        .branch() \
        .search_if('persistent.havetestresults == True') \
        .branch() \
        .search_if('bryce2unplayed == False') \
        .hook_to('passontestresults',
            return_link=False,
            condition='blood == False') \


def adine():
    ml.find_label('chapter5').search_if('persistent.adinegoodending == False').hook_to('impermanence_four_adine_killer')


def anna():
    condition = 'annastatus in ["bad", "abandoned"] or (annastatus == "none" and persistent.impermanence_four_killer)'
    def mark_anna_for_death():
        renpy.store.annasurvives = False
        renpy.store.trueselectable = False

    def kill_anna():
        renpy.store.annasurvives = False
        renpy.store.annadead = True
        renpy.store.trueselectable = False

    ( ml.find_label('chapter3')
        .hook_function(mark_anna_for_death, condition=condition)
        .search_if('persistent.annagoodending == True')
        .branch()
        .search_python('annasurvives = True')
        .hook_function(func=kill_anna, condition=condition)
    )


def bryce():
    brycecardif = ml.find_label('chapter4').search_if('persistent.brycegoodending == False')
    brycecardif.branch().search_if('totalinv <= 6').link_from('impermanence_four_bryce_c4card')
    brycecardif.add_entry('persistent.impermanence_four_no_reenlightenment == True',jump='impermanence_four_bryce_c4card')

    bryceif = ml.find_label('passontestresults').search_if('persistent.brycegoodending == True')

    brycefirstif = bryceif \
        .branch_else() \
        .search_say("I go in, and you stay here, alright?") \
        .link_from('impermanence_four_brycebad') \
        .search_menu("Let me go in first.") \
        .branch() \
        .search_if('persistent.brycegoodending == True')
    brycefirstif.branch_else().search_say("That's a very good point and all, but it's just too dangerous for you to go inside. I can't let anything happen to you, so we'll do it as I said.").link_from('impermanence_four_brycefirstbad')
    brycefirstif.add_entry('totalinv <= 6',jump='impermanence_four_brycefirstbad',before='persistent.brycegoodending == True')

    bryceif.add_entry('totalinv <= 10',jump='impermanence_four_brycebad',before='persistent.brycegoodending == True')

    brycefirstlabelif = ml.find_label('brycefirst').search_if('persistent.brycegoodending == True')
    brycefirstlabelif.branch_else().search_say("I watched as Bryce made his way to the front door. Looking around, I scanned the windows of the building for any sign of movement.").link_from('impermanence_four_brycefirstlabelbad')
    brycefirstlabelif.branch().hook_to('impermanence_four_brycefirstlabelbad', return_link=False)

    # Save Bryce from the timeline glitch if you've completed Bryce's good ending.
    ( ml.find_label('mcfirst')
        .search_with('dissolve')
        .hook_to('didit', return_link=False, condition='persistent.brycegoodending == True')
    )


def remy():
    # Chapter 2
    ( ml.find_label('_call_skipcheck_34')
        .hook_to('impermanence_four_remy_c2picturesseenskip')
    )

    # Chapter 3
    ( ml.find_label('remy3skip1')
        .search_if('persistent.endingsseen > 0')
        .branch()
        .search_if('persistent.playedadine2 == True')
        .hook_to('impermanence_four_remy_c3endingmenu')
    )

    # Chapter 4 death
    remcardif = ml.find_label('chapter4').search_if('persistent.remygoodending == False')
    remcardif.branch().search_if('remystatus == "bad"').link_from('impermanence_four_remy_c4card')
    remcardif.add_else_entry(jump='impermanence_four_remy_c4card')

    remfoundpause = ml.find_label('c4library') \
        .search_python('renpy.pause (3.3)')
    ( remfoundpause.search_if('persistent.remygoodending == True')
        .branch_else()
        .first()
        .link_from('impermanence_four_remy_c4library_dead')
    )
    remfoundpause.hook_to('impermanence_four_remy_c4library_dead', condition='remystatus=="bad" or remystatus=="abandoned"', return_link=False)

    rempostif = ml.find_label('c4postsections').search_if('persistent.remygoodending == False')
    rempostif.branch().search_if('remystatus == "abandoned"').link_from('impermanence_four_remy_c4postsections')
    rempostif.add_else_entry(jump='impermanence_four_remy_c4postsections')

    # Chapter 5 death
    ml.find_label('chapter5').search_if('persistent.remygoodending == False').hook_to('impermanence_four_remy_c5_killer')


def vara():
    adineif = ( 
        ml.find_label('c4hatchery')
        .search_if('adinestatus == "none"')
    )

    # Set label for jumping back persistent.remygoodending with adinestatus=="none"
    ( adineif
        .branch('adinestatus == "none"')
        .search_if('remygoodending == True')
        .branch()
        .search_say("Looks like you took my advice.")
        .link_from('impermanence_four_varadead_hatchery_adinestatusnone_remychat')
        .search_say("I think we should go inside.")
        .link_from('impermanence_four_varadead_hatchery_adinestatusnone_goinside')
    )
    # Jump back persistent.remygoodending with adinnestatus=="none"
    ( adineif
        .branch('adinestatus == "none"')
        .search_if('persistent.remygoodending == True')
        .branch()
        .search_say("Good job, [player_name].")
        .hook_to('impermanence_four_varadead_hatchery_adinestatusnone_remychat', return_link=False, condition='varasaved == False and (persistent.varasaved == False or persistent.impermanence_four_killer)')
    )
    # Jump over vara in hatchery remygoodending with adinnestatus=="none"
    ( adineif
        .branch('adinestatus == "none"')
        .search_if('remygoodending == True')
        .branch()
        .search_say("I'm glad we did. It was long overdue.")
        .hook_to('impermanence_four_varadead_hatchery_adinestatusnone_goinside', return_link=False, condition='varasaved == False and (persistent.varasaved == False or persistent.impermanence_four_killer)')
    )

        # Set label for jumping back persistent.remygoodending with adinestatus=="none"
    ( adineif
        .branch_else()
        .search_if('remygoodending == True')
        .branch()
        .search_say("Looks like you took my advice.")
        .link_from('impermanence_four_varadead_hatchery_adinestatusneutralgood_remychat')
        .search_say("I think we should go inside.")
        .link_from('impermanence_four_varadead_hatchery_adinestatusneutralgood_goinside')
    )
    # Jump back persistent.remygoodending with adinnestatus=="none"
    ( adineif
        .branch_else()
        .search_if('persistent.remygoodending == True')
        .branch()
        .search_say("Good job, [player_name].")
        .hook_to('impermanence_four_varadead_hatchery_adinestatusneutralgood_remychat', return_link=False, condition='varasaved == False and (persistent.varasaved == False or persistent.impermanence_four_killer)')
    )
    # Jump over vara in hatchery remygoodending with adinnestatus=="none"
    ( adineif
        .branch_else()
        .search_if('remygoodending == True')
        .branch()
        .search_say("I'm glad we did. It was long overdue.")
        .hook_to('impermanence_four_varadead_hatchery_adinestatusneutralgood_goinside', return_link=False, condition='varasaved == False and (persistent.varasaved == False or persistent.impermanence_four_killer)')
    )

    bryce4varasaved_line_before = ml.find_label('bryce4').search_say("How could someone ever get used to this? It's my duty, you know. But I can't save them all. Never could.", depth=300)
    ( bryce4varasaved_line_before
        .search_if('varasaved == False',depth=3)
        .branch()
        .search_say("You know what happened out on patrol today? We found a dead child and her mother in their home in the outskirts of town.")
        .link_from('impermanence_four_vara_bryce4_dead')
    )
    bryce4varasaved_line_before.hook_to('impermanence_four_vara_bryce4_dead',return_link=False,condition='varasaved == False and (persistent.varasaved == False or persistent.impermanence_four_killer)')


def sebastian():
    seb_complains = (
        ml.find_label('c4cont2')
        .search_if('mcfirst == True')
        .branch()
        .search_say("Yes, it has a great tradition behind it. What peeves me most is that I'll be on guard duty when it happens this year, so I probably won't be able to see a thing.")
    )

    ( seb_complains.search_if('persistent.sebastianplayed == True')
        .branch()
        .search_menu("I'll be sure not to miss it then.")
        .link_from('impermanence_four_sebastian_choice')
    )

    seb_complains.hook_to('impermanence_four_sebastian_choice', return_link=False, condition='persistent.sebastianplayed == True')


def trueending_killer():
    def trueending_killer_func():
        renpy.store.trueselectable = False
        renpy.store.cardenlightenment = False
        renpy.store.cardloss = True
    args = {'func':trueending_killer_func,'condition':'any([adinedead, annadead, brycedead, loremdead, remydead])'}

    for label in ['c3cont', 'c3contx']:
        ml.find_label(label).hook_function(**args)

    ( ml.find_label('chapter4')
        .search_python('_dismiss_pause = False')
        .hook_function(**args)
    )

    ( ml.find_label('brycefirst')
        .search_if('persistent.brycegoodending == True')
        .branch_else()
        .search_python('brycedead = True')
        .hook_function(**args)
    )

    ( ml.find_label('impermanence_four_remy_c4library_dead')
        .search_python('remydead = True')
        .hook_function(**args)
    )

    ( ml.find_label('c4postsections')
        .search_python('renpy.pause (2.0)')
        .hook_function(**args)
    )

    ( ml.find_label('chapter5')
        .search_python('_dismiss_pause = False')
        .hook_function(**args)
        .search_say("(Today is the day of the big fireworks. Who shall I bring?)")
        .hook_function(**args)
    )


@loadable_mod
class AwSWImpermanenceMod(Mod):
    name = "Impermanence"
    author = "4onen"
    version = "v0.0"
    dependencies = ["MagmaLink","?A Solitary Mind"]

    @classmethod
    def mod_load(cls):
        ml.register_mod_settings(cls, screen='impermanence_four_modsettings')
        no_reenlightenment()
        testresults()
        adine()
        anna()
        remy()
        bryce()
        sebastian()
        vara()

        trueending_killer()

    @staticmethod
    def mod_complete():
        pass