
from header import *

def dialogs_tutorials(dialogs):
  dialogs.extend([

    [anyone, "fighter_pretalk", [], "Tell me what kind of practice you want.", "fighter_talk", []],
    
	## happy begin
    ## tutorial_fighter begin
    ## fighter_talk ( can direct move to main_ops )
    [anyone|plyr, "fighter_talk",
    [
        (is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
    ], "I want to practice attacking.", "fighter_talk_train_attack", []],
    [anyone|plyr, "fighter_talk",
    [
        (is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
    ], "I want to practice blocking with my weapon.", "fighter_talk_train_parry", []],
    [anyone|plyr, "fighter_talk",
    [
        (is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
    ], "Let's do some sparring practice.", "fighter_talk_train_combat", []],
    [anyone|plyr, "fighter_talk",
    [
        (is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
        (eq,1,0)
    ], "{!}TODO: Let's train chamber blocking.", "fighter_talk_train_chamber", []],
    [anyone|plyr, "fighter_talk",
    [
        (is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
    ], "[Leave]", "close_window", []],
    ## tutorial_fighter end
	## happy end
    
    [anyone, "fighter_talk_train_attack",
    [
        (get_player_agent_no, ":player_agent"),
        (agent_has_item_equipped, ":player_agent", "itm_practice_sword"), #TODO: add other melee weapons
    ], "All right. There are four principle directions for attacking. These are overhead swing, right swing, left swing and thrust.\
 Now, I will tell you which direction to attack from and you must try to do the correct attack.\
 ^^(Move your mouse while you press the left mouse button to specify attack direction. For example, to execute an overhead attack, move the mouse up at the instant you press the left mouse button.\
 The icons on your screen will help you do the correct action.)" , "fighter_talk_train_attack_2", []],

    [anyone|plyr, "fighter_talk_train_attack_2",  [],
    "Let's begin then. I am ready.", "close_window",
    [
        (assign, "$g_tutorial_training_ground_melee_trainer_attack", "$g_talk_troop"),
        (assign, "$g_tutorial_training_ground_melee_state", 0),
        (assign, "$g_tutorial_training_ground_melee_trainer_action_state", 0),
        (assign, "$g_tutorial_training_ground_current_score", 0),
        (assign, "$g_tutorial_training_ground_current_score_2", 0),
        (assign, "$g_tutorial_update_mouse_presentation", 0),
    ]],

    [anyone|plyr, "fighter_talk_train_attack_2", [], "Actually I want to do something else.", "fighter_pretalk", []],

    [anyone, "fighter_talk_train_attack",
    [
        (str_store_string, s3, "str_tutorial_training_ground_warning_no_weapon"),
    ], "{!}{s3}", "close_window", []],

    [anyone, "fighter_talk_train_parry",
    [
        (get_player_agent_no, ":player_agent"),
        (agent_has_item_equipped, ":player_agent", "itm_practice_sword"), #TODO: add other melee weapons
    ], "Unlike a shield, blocking with a weapon can only stop attacks coming from one direction.\
 For example if you block up, you'll deflect overhead attacks, but you can still be hit by side swings or thrust attacks.\
 ^^(You must press and hold down the right mouse button to block.)", "fighter_talk_train_parry_2", []],

	[anyone, "fighter_talk_train_parry_2", [], "I'll now attack you with different types of strokes, and I will wait until you do the correct block before attacking.\
 Try to do the correct block as soon as you can.\
 ^^(This practice is easy to do with the 'automatic block direction' setting which is the default.\
 If you go to the Options menu and change defend direction control to 'mouse movement' or 'keyboard', you'll need to manually choose block direction. This is much more challenging, but makes the game much more interesting.\
 This practice can be very useful if you use manual blocking.)", "fighter_talk_train_parry_3", []],
	 
    [anyone|plyr, "fighter_talk_train_parry_3",  [], "Let's begin then. I am ready.", "close_window",
    [
        (assign, "$g_tutorial_training_ground_melee_trainer_parry", "$g_talk_troop"),
        (assign, "$g_tutorial_training_ground_melee_state", 0),
        (assign, "$g_tutorial_training_ground_melee_trainer_action_state", 0),
        (assign, "$g_tutorial_training_ground_current_score", 0),
    ]],

    [anyone|plyr, "fighter_talk_train_parry_3",  [], "Actually I want to do something else.", "fighter_pretalk", []],
	 
    [anyone, "fighter_talk_train_parry",
    [
        (str_store_string, s3, "str_tutorial_training_ground_warning_no_weapon"),
    ], "{!}{s3}", "close_window", []],

    [anyone, "fighter_talk_train_chamber",
    [
        (get_player_agent_no, ":player_agent"),
        (agent_has_item_equipped, ":player_agent", "itm_practice_sword"), #TODO: add other melee weapons
    ], "{!}TODO: OK.", "close_window",
    [
        (assign, "$g_tutorial_training_ground_melee_trainer_chamber", "$g_talk_troop"),
        (assign, "$g_tutorial_training_ground_melee_state", 0),
        (assign, "$g_tutorial_training_ground_melee_trainer_action_state", 0),
        (assign, "$g_tutorial_training_ground_current_score", 0),
    ]],

    [anyone, "fighter_talk_train_chamber",
    [
        (str_store_string, s3, "str_tutorial_training_ground_warning_no_weapon"),
    ], "{!}{s3}", "close_window", []],

    [anyone, "fighter_talk_train_combat",
    [
        (get_player_agent_no, ":player_agent"),
        (agent_has_item_equipped, ":player_agent", "itm_practice_sword"), #TODO: add other melee weapons
    ], "Sparring is an excellent way to prepare for actual combat.\
 We'll fight each other with non-lethal weapons now, until one of us falls to the ground.\
 You can get some bruises of course, but better that than being cut down in the real thing.", "fighter_talk_train_combat_2", []],

    [anyone|plyr, "fighter_talk_train_combat_2",  [], "Let's begin then. I am ready.", "close_window",
    [
        (assign, "$g_tutorial_training_ground_melee_trainer_combat", "$g_talk_troop"),
        (assign, "$g_tutorial_training_ground_melee_state", 0),
        (assign, "$g_tutorial_training_ground_melee_trainer_action_state", 0),
    ]],

    [anyone|plyr, "fighter_talk_train_combat_2",  [], "Actually I want to do something else.", "fighter_pretalk", []],
	 
    [anyone, "fighter_talk_train_combat",
    [
        (str_store_string, s3, "str_tutorial_training_ground_warning_no_weapon"),
    ], "{!}{s3}", "close_window", []],

   
    
    [anyone|plyr, "fighter_parry_try_again", [], "Yes. Let's try again.", "fighter_talk_train_parry", []],

    [anyone|plyr, "fighter_parry_try_again", [], "No, I think I am done for now.", "fighter_talk_leave_parry", []],
    
    [anyone|plyr, "fighter_parry_warn", [], "I am sorry. Let's try once again.", "fighter_talk_train_parry", []],

    [anyone|plyr, "fighter_parry_warn", [], "Sorry. I must leave this practice now.", "fighter_talk_leave_parry", []],

    [anyone, "fighter_talk_leave_parry", [], "All right. As you wish.", "close_window", []],
	 
    [anyone|plyr, "fighter_combat_try_again", [], "Yes. Let's do another round.", "fighter_talk_train_combat", []],

    [anyone|plyr, "fighter_combat_try_again", [], "No. That was enough for me.", "fighter_talk_leave_combat", []],

    [anyone, "fighter_talk_leave_combat", [], "Well, all right. Talk to me again if you change your mind.", "close_window", []],

    # [anyone|plyr, "fighter_chamber_try_again",
    # [],
    # "{!}TODO: OK let's try again.", "fighter_talk_train_chamber", []],

    # [anyone|plyr, "fighter_chamber_try_again",
    # [],
    # "TODO: No, let's leave it there.", "fighter_talk_leave_chamber", []],

    # [anyone, "fighter_talk_leave_chamber",
    # [],
    # "{!}TODO: OK. Bye.", "close_window", []],
    
    # unused
    [anyone|plyr, "fighter_chamber_warn", [], "{!}TODO: Sorry, let's try once again.", "fighter_talk_train_chamber", []],

    # unused
    [anyone|plyr, "fighter_chamber_warn", [], "{!}TODO: Sorry. I want to leave the exercise.", "close_window", []],
	 
    [trp_tutorial_master_archer, "ranged_end", [], "Now, you can go talk with the melee fighters or the horsemanship trainer if you haven't already done so. They can teach you important skills too.", "close_window", []],

    [anyone|plyr, "archer_talk",
    [
        (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 0),
    ], "Yes, show me how to use ranged weapons.", "archer_challenge", []],

    # [anyone|plyr, "archer_talk",
    # [
     # (gt, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 0),
     # ],
    # "{!}TODO: I want to move to the next stage.", "archer_challenge", []],

    [anyone|plyr, "archer_talk", [], "No, not now.", "close_window", []],

    [trp_tutorial_master_archer, "archer_challenge",
    [
        (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 0),
    ], "All right. Your first training will be in bowmanship. The bow is a difficult weapon to master. But once you are sufficiently good at it, you can shoot quickly and with great power.\
 Go pick up the bow and arrows you see over there now and shoot those targets.", "archer_challenge_2", []],

    # [trp_tutorial_master_archer, "archer_challenge",
    # [
     # (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 1),
     # ],
    # "{!}TODO: Make 3 shots with crossbow.", "archer_challenge_2",
    # []],

    # [trp_tutorial_master_archer, "archer_challenge",
    # [],
    # "{!}TODO: Make 3 shots with javelin.", "archer_challenge_2",
    # []],

    [anyone|plyr, "archer_challenge_2", [], "All right. I am ready.", "close_window",
    [
        (assign, "$g_tutorial_training_ground_archer_trainer_state", 1),
        (try_begin),
            (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 0),
            (assign, "$g_tutorial_training_ground_archer_trainer_item_1", "itm_practice_bow"),
            (assign, "$g_tutorial_training_ground_archer_trainer_item_2", "itm_practice_arrows"),
        (else_try),
            (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 1),
            (assign, "$g_tutorial_training_ground_archer_trainer_item_1", "itm_practice_crossbow"),
            (assign, "$g_tutorial_training_ground_archer_trainer_item_2", "itm_practice_bolts"),
        (else_try),
            (assign, "$g_tutorial_training_ground_archer_trainer_item_1", "itm_practice_javelin"),
            (assign, "$g_tutorial_training_ground_archer_trainer_item_2", -1),
        (try_end),
    ]],

    [anyone|plyr, "archer_challenge_2", [], "Just a minute. I want to do something else first.", "close_window", []],

    [trp_tutorial_master_horseman, "horsemanship_end", [], "Now, you can go talk with the melee fighters or the archery trainer if you haven't already done so. You need to learn everything you can to be prepared when you have to defend yourself.", "close_window", []],
	
    [anyone|plyr, "horseman_talk", [], "Yes, I would like to practice riding.", "horseman_challenge", []],

    [anyone|plyr, "horseman_talk", [], "Uhm. Maybe later.", "close_window", []],

  # [trp_tutorial_master_horseman, "horseman_challenge",
   # [
     # (eq, "$g_tutorial_training_ground_player_continue_without_basics", 0),
     # (this_or_next|eq, "$g_tutorial_training_ground_melee_trainer_attack_completed", 0),
     # (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 0),
    # ],
   # "Hmm. Do you know how to use your weapons? You'd better learn to use those on foot before you start to train using them on horseback.", "horseman_ask",
   # []],

  # [anyone|plyr, "horseman_ask",
   # [],
   # "Yes, I know ", "horseman_challenge",
   # [
     # (assign, "$g_tutorial_training_ground_player_continue_without_basics", 1),
     # ]],

  # [anyone|plyr, "horseman_ask",
   # [],
   # "{!}TODO: No", "horseman_ask_2",
   # []],

  # [trp_tutorial_master_horseman, "horseman_ask_2",
   # [],
   # "{!}TODO: Come back later then.", "close_window",
   # []],

    [trp_tutorial_master_horseman, "horseman_challenge",
    [
        (eq, "$g_tutorial_training_ground_horseman_trainer_completed_chapters", 0),
    ], "Good. Now, I will give you a few exercises that'll teach you riding and horseback weapon use.\
 Your first assignment is simple. Just take your horse for a ride around the course.\
 Go as slow or as fast as you like.\
 Come back when you feel confident as a rider and I'll give you some tougher exercises.", "horseman_melee_challenge_2",
    []],

    [anyone|plyr, "horseman_melee_challenge_2", [], "All right. I am ready.", "close_window",
    [
        (assign, "$g_tutorial_training_ground_horseman_trainer_state", 1),
        (try_begin),
            (eq, "$g_tutorial_training_ground_horseman_trainer_completed_chapters", 0),
            (assign, "$g_tutorial_training_ground_horseman_trainer_item_1", -1),
            (assign, "$g_tutorial_training_ground_horseman_trainer_item_2", -1),
        (else_try),
            (eq, "$g_tutorial_training_ground_horseman_trainer_completed_chapters", 1),
            (assign, "$g_tutorial_training_ground_horseman_trainer_item_1", "itm_arena_lance"),
            (assign, "$g_tutorial_training_ground_horseman_trainer_item_2", -1),
        (else_try),
            (assign, "$g_tutorial_training_ground_horseman_trainer_item_1", "itm_practice_bow_2"),
            (assign, "$g_tutorial_training_ground_horseman_trainer_item_2", "itm_practice_arrows_2"),
        (try_end),
    ]],
 
    [anyone|plyr, "horseman_melee_challenge_2", [], "Just a minute. I need to do something else first.", "close_window", []],

    [anyone, "tutorial_troop_default",
    [
        (try_begin),
            (eq, "$g_tutorial_training_ground_intro_message_being_displayed", 1),
            (assign, "$g_tutorial_training_ground_intro_message_being_displayed", 0),
            (tutorial_message, -1), #remove tutorial intro immediately before a conversation
        (try_end),
    ], "Hey, I am trying to practice here. Go, talk with the archery trainer if you need guidance about ranged weapons.", "close_window", []],


  ## end of file
  ])