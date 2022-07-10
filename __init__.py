from modloader.modclass import Mod, loadable_mod

import jz_magmalink as ml

def no_reenlightenment():
    args = {'condition':'persistent.impermanence_four_no_reenlightenment == True','return_link':False}
    ( ml.find_label('seccont')
        .search_if('persistent.trueending')
        .hook_to('impermanence_four_no_reenlightenment_c1',**args)
        .search_python('renpy.pause(4.0)')
        .link_from('impermanence_four_no_reenlightenment_c1_end')
    )

    ( ml.find_label('chapter2')
        .search_python('cardtrauma = False')
        .hook_to('impermanence_four_no_reenlightenment_c2',**args)
        .search_python('renpy.pause(2.0)')
        .link_from('impermanence_four_no_reenlightenment_c2_end')
    )

    ( ml.find_label('chapter3')
        .search_if('persistent.trueending == True')
        .add_entry(condition='persistent.impermanence_four_no_reenlightenment == True and trueselectable == True and persistent.trueending == False',
                   jump='impermanence_four_no_reenlightenment_c3',
                   before='persistent.trueending == True')
        .link_behind_from('impermanence_four_no_reenlightenment_c3_end')
    )

    ( ml.find_label('chapter4')
        .search_if('persistent.trueending == True')
        .add_entry(condition='persistent.impermanence_four_no_reenlightenment == True and trueselectable == True and persistent.trueending == False',
                    jump='impermanence_four_no_reenlightenment_c4',
                    before='persistent.trueending == True')
        .link_behind_from('impermanence_four_no_reenlightenment_c4_end')
    )

    ( ml.find_label('chapter5')
        .search_if('persistent.trueending')
        .add_entry(condition='persistent.impermanence_four_no_reenlightenment == True and trueselectable == True and persistent.trueending == False',
                    jump='impermanence_four_no_reenlightenment_c5',
                    before='persistent.trueending')
        .link_behind_from('impermanence_four_no_reenlightenment_c5_end')
    )


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
    

    bryce4varasavedif = ml.find_label('bryce4').search_if('varasaved == False')
    bryce4varasavedif.branch().search_say("You know what happened out on patrol today? We found a dead child and her mother in their home in the outskirts of town.").link_from('impermanence_four_vara_bryce4_dead')
    bryce4varasavedif.branch_else().hook_to('impermanence_four_vara_bryce4_dead',return_link=False,condition='varasaved == False and (persistent.varasaved == False or persistent.impermanence_four_killer)')


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
        remy()
        bryce()
        sebastian()

    @staticmethod
    def mod_complete():
        pass