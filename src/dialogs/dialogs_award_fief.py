
from header import *

def dialogs_award_fief(dialogs):
  dialogs.extend([
  
  
    [anyone, "event_triggered",
    [
        (eq, "$talk_context", tc_give_center_to_fief),

        (assign, ":there_are_vassals", 0),
        (assign, ":end_cond", npcs_end),
        (try_for_range, ":troop_no", npcs_begin, ":end_cond"),
            (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
            (neq, "trp_player", ":troop_no"),
            (store_troop_faction, ":faction_no", ":troop_no"),
            (eq, ":faction_no", "fac_player_supporters_faction"),
            (val_add, ":there_are_vassals", 1),
            (assign, ":end_cond", 0),
        (try_end),
     
        (try_begin),
            (gt, ":there_are_vassals", 0),
            (str_store_string, s2, "str_do_you_wish_to_award_it_to_one_of_your_vassals"),
        (else_try),
            (str_store_string, s2, "str_who_do_you_wish_to_give_it_to"),
        (try_end),

        (str_store_party_name, s1, "$g_center_taken_by_player_faction"),
        (str_store_string, s5, "str_sire_my_lady_we_have_taken_s1_s2"),
    ], "{!}{s5}", "award_fief_to_vassal", []],

    [anyone|plyr, "award_fief_to_vassal",
    [
        (is_between, "$g_player_court", centers_begin, centers_end), 
        (store_faction_of_party, ":player_court_faction", "$g_player_court"),
        (eq, ":player_court_faction", "fac_player_supporters_faction"),
	], "I wish to defer the appointment of a lord, until I take the counsel of my subjects", "award_fief_to_vassal_defer", []],

    [anyone, "award_fief_to_vassal_defer", [], "As you wish, {sire/my lady}. You may decide this matter at a later date.", "close_window",
    [
        (try_begin),
            (faction_slot_eq, "$players_kingdom", slot_faction_political_issue, -1),
            (faction_set_slot, "$players_kingdom", slot_faction_political_issue, "$g_center_taken_by_player_faction"),
        (try_end),
        (call_script, "script_give_center_to_lord", "$g_center_taken_by_player_faction", -1, 0), #-1 for the faction lord in this script is used exclusively in this context
        #It is only used because script_give_center_to_faction does not reset the town lord if fac_player_supporters_faction is the attacker

        (assign, "$g_center_taken_by_player_faction", -1),
	 
        #new start
        (try_begin),
            (eq, "$g_next_menu", "mnu_castle_taken"), 
            (jump_to_menu, "$g_next_menu"),
        (try_end),  
        #new end
    ]],
   
    [anyone|plyr|repeat_for_troops, "award_fief_to_vassal",
    [
        (store_repeat_object, ":troop_no"),
        (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
        (neq, "trp_player", ":troop_no"),
        (store_troop_faction, ":faction_no", ":troop_no"),
        (eq, ":faction_no", "fac_player_supporters_faction"),
        (str_store_troop_name, s11, ":troop_no"),
        (call_script, "script_print_troop_owned_centers_in_numbers_to_s0", ":troop_no"),

        (try_begin),
            (troop_slot_eq, "$g_talk_troop", slot_lord_recruitment_argument, argument_benefit),
            (str_store_string, s12, "str__promised_fief"),
        (else_try),
            (str_clear, s12),
        (try_end),

        (try_begin),
            (eq, reg0, 0),
            (str_store_string, s1, "str_no_fiefss12"),
        (else_try),
            (str_store_string, s1, "str_fiefs_s0s12"),
        (try_end),
    ], "{!}{s11} {s1}.", "award_fief_to_vassal_2",
    [
        (store_repeat_object, "$temp")
    ]],

    [anyone|plyr, "award_fief_to_vassal",
    [
        (call_script, "script_print_troop_owned_centers_in_numbers_to_s0", "trp_player"),
        (str_store_party_name, s1, "$g_center_taken_by_player_faction"),

        (try_begin),
            (eq, "$g_talk_troop", "$supported_pretender"),
            (str_store_string, s12, "str_please_s65_"),
        (else_try),	
            (str_clear, s12),
        (try_end),	
	 
        (assign, ":there_are_vassals", 0),
        (assign, ":end_cond", npcs_end),
        (try_for_range, ":troop_no", npcs_begin, ":end_cond"),
            (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
            (neq, "trp_player", ":troop_no"),
            (store_troop_faction, ":faction_no", ":troop_no"),
            (eq, ":faction_no", "fac_player_supporters_faction"),
            (val_add, ":there_are_vassals", 1),
            (assign, ":end_cond", 0),
        (try_end),
     
        (try_begin),
            (gt, ":there_are_vassals", 0),
            (str_store_string, s2, "str_fiefs_s0"),
        (else_try),
            (str_clear, s2),
        (try_end),
  	 
        (str_store_string, s5, "str_s12i_want_to_have_s1_for_myself"),
	 ], "{!}{s5}", "award_fief_to_vassal_2",      
    [
        (assign, "$temp", "trp_player"),
    ]],  

    [anyone, "award_fief_to_vassal_2", [], "As you wish, {sire/my lady}. {reg6?I:{reg7?You:{s11}}} will be the new {reg3?lady:lord} of {s1}.", "close_window",
    [
        (assign, ":new_owner", "$temp"),
	 
        (call_script, "script_give_center_to_lord", "$g_center_taken_by_player_faction", ":new_owner", 0),
        (try_begin),
            (faction_slot_eq, "$players_kingdom", slot_faction_political_issue, "$g_center_taken_by_player_faction"),
            (faction_set_slot, "$players_kingdom", slot_faction_political_issue, -1),
        (try_end),
   
        (assign, reg6, 0),
        (assign, reg7, 0),
        (try_begin),
            (eq, ":new_owner", "$g_talk_troop"),
            (assign, reg6, 1),
        (else_try),
            (eq, ":new_owner", "trp_player"),
            (assign, reg7, 1),
        (else_try),
            (str_store_troop_name, s11, ":new_owner"),
        (try_end),
        (str_store_party_name, s1, "$g_center_taken_by_player_faction"),
        (troop_get_type, reg3, ":new_owner"),
     
        (assign, "$g_center_taken_by_player_faction", -1),	 	           

        #new start
        (try_begin),
            (eq, "$g_next_menu", "mnu_castle_taken"), 
            (jump_to_menu, "$g_next_menu"),
        (try_end),  
        #new end
    ]],

    # Awarding fiefs in rebellion...
    [anyone, "event_triggered",
    [
        (faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "$g_talk_troop"),
        (ge, "$g_center_taken_by_player_faction", 0),
        (str_store_party_name, s1, "$g_center_taken_by_player_faction"),
    ], "{s1} is not being managed by anyone. Whom shall I put in charge?", "center_captured_rebellion", []],

    [anyone|plyr|repeat_for_troops, "center_captured_rebellion",
    [
        (store_repeat_object, ":troop_no"),
        (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
        (neq, "$g_talk_troop", ":troop_no"),
        (neq, "trp_player", ":troop_no"),
        (store_troop_faction, ":faction_no", ":troop_no"),
        (eq, ":faction_no", "fac_player_supporters_faction"),
        (str_store_troop_name, s11, ":troop_no"),
        (call_script, "script_print_troop_owned_centers_in_numbers_to_s0", ":troop_no"),
        (try_begin),
            (eq, reg0, 0),
            (str_store_string, s1, "@(no fiefs)"),
        (else_try),
            (str_store_string, s1, "@(fiefs: {s0})"),
        (try_end),
    ], "{s11}. {s1}", "center_captured_rebellion_2",
    [
        (store_repeat_object, "$temp"),
    ]],

    [anyone|plyr, "center_captured_rebellion",
    [
        (call_script, "script_print_troop_owned_centers_in_numbers_to_s0", "trp_player"),
        (str_store_party_name, s1, "$g_center_taken_by_player_faction"),
    ], "Please {s65}, I want to have {s1} for myself. (fiefs: {s0})", "center_captured_rebellion_2",
    [
        (assign, "$temp", "trp_player"),
    ]],

    [anyone|plyr, "center_captured_rebellion",
    [
        (call_script, "script_print_troop_owned_centers_in_numbers_to_s0", "$g_talk_troop"),
        (str_store_party_name, s1, "$g_center_taken_by_player_faction"),
    ], "{s66}, you should have {s1} for yourself. (fiefs: {s0})", "center_captured_rebellion_2",
    [
        (assign, "$temp", "$g_talk_troop"),
    ]],

    [anyone, "center_captured_rebellion_2",
    [
#     (faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "$g_talk_troop"),
#     (ge, "$g_center_taken_by_player_faction", 0),
    ], "Hmmm. All right, {playername}. I value your counsel highly. {reg6?I:{reg7?You:{s11}}} will be the new {reg3?lady:lord} of {s1}.", "close_window",
    [
        (assign, ":new_owner", "$temp"),
        (call_script, "script_calculate_troop_score_for_center", ":new_owner", "$g_center_taken_by_player_faction"),
        (assign, ":new_owner_score", reg0),
        (assign, ":total_negative_effect"),
        (try_for_range, ":cur_troop", npcs_begin, npcs_end),
            (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),     
            (store_troop_faction, ":cur_faction", ":cur_troop"),
            (eq, ":cur_faction", "fac_player_supporters_faction"),
            (neq, ":cur_troop", ":new_owner"),
            (neg|troop_slot_eq, ":cur_troop", slot_troop_stance_on_faction_issue, ":new_owner"),
            (call_script, "script_troop_get_relation_with_troop", ":cur_troop", ":new_owner"),
            (lt, reg0, 25),

            (call_script, "script_calculate_troop_score_for_center", ":cur_troop", "$g_center_taken_by_player_faction"),
            (assign, ":cur_troop_score", reg0),
            (gt, ":cur_troop_score", ":new_owner_score"),
            (store_sub, ":difference", ":cur_troop_score", ":new_owner_score"),
            (store_random_in_range, ":random_dif", 0, ":difference"),
            (val_div, ":random_dif", 1000),
            (gt, ":random_dif", 0),
            (val_add, ":total_negative_effect", ":random_dif"),
            (val_mul, ":random_dif", -1),
            (call_script, "script_change_player_relation_with_troop", ":cur_troop", ":random_dif"),
        (try_end),
        (val_mul, ":total_negative_effect", 2),
        (val_div, ":total_negative_effect", 3),
        (val_add, ":total_negative_effect", 5),
        (try_begin),
            (neq, ":new_owner", "trp_player"),
            (val_min, ":total_negative_effect", 30),
            (call_script, "script_change_player_relation_with_troop", ":new_owner", ":total_negative_effect"),
        (try_end),
     
        (call_script, "script_give_center_to_lord", "$g_center_taken_by_player_faction", ":new_owner", 0),
        (try_begin),
            (faction_slot_eq, "$players_kingdom", slot_faction_political_issue, "$g_center_taken_by_player_faction"),
            (faction_set_slot, "$players_kingdom", slot_faction_political_issue, -1),
        (try_end),
	    
        (assign, reg6, 0),
        (assign, reg7, 0),
        (try_begin),
            (eq, ":new_owner", "$g_talk_troop"),
            (assign, reg6, 1),
        (else_try),
            (eq, ":new_owner", "trp_player"),
            (assign, reg7, 1),
        (else_try),
            (str_store_troop_name, s11, ":new_owner"),
        (try_end),
        (str_store_party_name, s1, "$g_center_taken_by_player_faction"),
        (troop_get_type, reg3, ":new_owner"),
     
        (assign, "$g_center_taken_by_player_faction", -1),	 	           

        #new start
        (try_begin),
            (eq, "$g_next_menu", "mnu_castle_taken"), 
            (jump_to_menu, "$g_next_menu"),
        (try_end),  
        #new end
    ]],
    
  ## end of file
  ])
