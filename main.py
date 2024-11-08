from groupme_api import get_groups, get_member_ids
from removal import nuke_group
from scheduler import run_scheduler

# Get groups
groups = get_groups()
if groups:
    print("Groups available:")
    for i, group in enumerate(groups, 1):
        print(f"{i}: {group['name']} (ID: {group['id']})")
    selected_group_index = int(input("Please specify the number of the group to manage: ")) - 1
    GROUP_ID = groups[selected_group_index]['id']
    GROUP_NAME = groups[selected_group_index]['name']
    
    # Ask for user input
    action = input(f"Enter 'nuke' to remove everyone from {GROUP_NAME}, or part of the name of the user to remove: ")
    
    if action.lower() == 'nuke':
        confirm = input("Are you sure you want to remove all members from the group? Type 'yes' to confirm: ")
        if confirm.lower() == 'yes':
            members = get_member_ids(GROUP_ID)
            nuke_group(GROUP_ID, members)
            print(f"All members have been removed from {GROUP_NAME}.")
        else:
            print("Nuke operation cancelled.")
    else:
        # Get matching members
        matching_members = get_member_ids(GROUP_ID, action)
        if matching_members:
            if len(matching_members) > 1:
                print("Multiple users found:")
                for i, member in enumerate(matching_members, 1):
                    print(f"{i}: {member['nickname']}")
                selected_index = int(input("Please specify the number of the user to remove: ")) - 1
                selected_member = matching_members[selected_index]
            else:
                selected_member = matching_members[0]
        
            USER_ID_TO_REMOVE = selected_member['id']
            USER_NAME_TO_REMOVE = selected_member['nickname']
            # Schedule removals
            run_scheduler(GROUP_ID, USER_ID_TO_REMOVE, USER_NAME_TO_REMOVE)
        else:
            print(f"User {action} not found in the group.")
else:
    print("No groups found.")
