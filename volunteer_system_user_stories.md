# Volunteer system

## User types

* Volunteer - People on the ground helping
* Trainer - Someone able to sign off volunteers as having received training for a specific role
* Manager - Check volunteers arrive for shifts, provide aid
* Admin - Create shifts/roles etc.

> I don't think we have Trainer or Manager separate from volunteer manager. 

## Shift types
Not the same as roles. Roles are e.g. "bar", "A/V" shifts are the specific combination of time, place & role.

* Normal - A time period, at a location where a role to be filled.
* Training - Special shift that the volunteer must complete before being allowed to do other shifts of that type (e.g. bar training)

> I don't think we've run training sessions scheduled via system, do we want this? I don't think there is a 

## Availability
Allow volunteers to indicate that they don't mind the specific role they perform.

* Free shift - The volunteer indicates that they are happy to be assigned any (normal) shift they are trained to do.
* Cover - the volunteer indicates that they are happy to be contacted to fill required shifts if need be.

> Thinking to cover this with new role giving pool of people to 
> * provide cover where other shifts are short
> * Do one off tasks
> * Cover recurring tasks/checks

As a volunteer I would like to:
-------------------------------
* View all roles
  > `/volunteer/choose-roles`
* View all shifts and filter by:
    - Role
    - Location
    - Shifts I can do (I have the training and pass the requirements)
    - Time
    - That I have signed up to
    - That don't clash with items in the schedule I've starred
  > `/volunteer/schedule?day=sat` `apps/volunteer/schedule.py` 
  
  > Currently hardcoded Fri/Sat/Sun/Mon
  
  > Don't have filters? There is a `filter-panel` in the template should some js be populating it?
  
  > Lists all shifts without filtering by which roles user is interested/trained in?
  
  > Links to other days in tab content don't work
  
  > Possibly a lot of this is from JS not running? https://github.com/emfcamp/Website/issues/868#issuecomment-586746500
  
  > Would be nice to have schedule show shifts you're signed up for - currently "Sign Up" button would become a "Cancel" button, is that enough?
* Sign up for:
    - A specific shift I have been trained for
    - A training session
    - A shift I have not been trained for:
        + ONLY if I can receive training before the shift starts
    > Signup is broken -> CSRF not right for the form? https://github.com/emfcamp/Website/issues/868
    > Only training check has hardcoded `if role == Bar`, and doesn't allow sign up till training is done
* Indicate availability
    - For a free shift (whole shifts only?)
    - For cover (possibly allow partial shifts?)
    > Not implemented? Do we still want this? Or going to be covering with runner pool?
* Be notified
    - About:
        + My upcoming shifts
        + Changes to my shift
        + Shifts that need covering
        + Details of shift I have been assigned (if I signed up as 'free')
            * Ideally 15 min before the shift starts
    - By:
        + Email
        + SMS
        + Notification page on site
        + Push notification (from web app or native app)
    > I don't think there are any automatic notifications? Manually sent emails discussed below in manager section. Do we want automatic notifications? Would need to properly flesh out opting in for them in sign up flow. 
* Be able to change my notification settings
* Be able to communicate with managers and/or an admin
* Provide extra information
    - Phone number
    > Phone number is currently required to sign up as a volunteer (though there is no check that the number given is real). I'd like to remove that requirement. I'm thinking email address as only required contact details and optional fields for phone number (for public and eventphone system), IRC nick or other contact details. 
    - Age
    - Misc details (e.g. experience)
* When on shift
    - Log that my replacement has not arrived on time (if unmanaged)
    - Request help at any time
    - Have access to information about the role
    > I don't think we have anything for these at the moment. I'm not sure about putting first two in system - rather they are just "contact volunteer desk"
* Change a shift
    - And be alerted if doing so will flag me as a no-show for that shift (i.e. if I try to change a shift within 15 min of its start)
  > Looks like there is processing to cancel doing a shift (button on sign up page toggles if you're signed up for the shift or not) but nothing to check time is far enough before start. 

> Currently default page for `/volunteer/` (what's linked from main site nav bar) is `/volunteer/account` probably better to make that be `/volunteer/schedule` after they've signed up. Can change that in `sign_up.py` L77 change to `redirect(url_for(".schedule"))` Do we want something else here for before the event? Are we going to allow signing up to volunteer system (and shifts) before event? I'm inclined towards: yes allowing people to sign up. 

As a trainer I would like to:
-----------------------------
* Approve a volunteer as trained for a role
* Sign up to train a training session (?)

> Marking people as trained is handled in `apps/volunteer/training.py` 
> Requires volunteer admin privileges
> Is pretty clunky - just shows list of all volunteers who're interested in role with checkbox for trained. 

> I think tracking training in volunteer system was only done for bar previously and it was auto ticked when they completed questions so this UI was never actually used. Is it going to be needed?

As a manager I would like to:
-----------------------------

> I don't think we have a role manager so most of this functionality is folded into volunteer admin. 

* Assign free volunteers to shifts
* Change who's on a shift (with and without flagging them as a no-show)
* Edit shift info
* Mark whether a volunteer attended their shift
* Respond to questions/concerns of volunteers
* Ban a volunteer (and record a reason) from
    - A role
    - All roles
  > We have a `Banned` boolean attached to a user but no provision for giving a reason, or it being only for some roles. Is this checked anywhere?
* View all volunteers that have signed up for a session
* Contact:
    - All volunteers
    - All volunteers with certain training
    - All volunteers who have signed up for a free shift
    - All volunteers who have indicated that they may do cover shifts
  > There is option to manually send email to volunteers at `notifications/emailvolunteers`
    
  > Currently broken with `notification/base.html` using `{% assets %}`. I've commented that out to be able to poke at it (without CSS) but need to fix it properly. Related: https://github.com/emfcamp/Website/issues/869
    
  > Currently only offers option to email all users interested in a role. Would really like 
  
  > Isn't limited to users who've checked `allow_comms_during_event`?

* View which volunteers are currently in which shifts
  > I think this will be  visible on `volunteer/shift/<id>`. Page has a "These people are on this shift" bit. But getting to there is only possible from schedule?
* View which current shifts require volunteers
* View which upcoming shifts require volunteers
  > `volunteer/schedule` shows count of signed up over needed. 


As an admin I would like to:
----------------------------
* Create roles with
    - Any requirements (e.g. age)
      > Only age requirement we support is over 18
    - A list of trainers
      > Don't have this? Notes above on if we need training in system. 
      > I'd like to add details of who to contact if you need help, can probably just be put in description. 
    - Minimum/maximum number of volunteers required per shift
    - A description
* Create venues with
    - A name
    - A location
    - Any other notes
* Create/Delete/Edit shifts
    - By:
        + Importing details (e.g. from frab, json)
        + Defining parameters
            * Time of the first shift
            * Shift duration
            * Number of shifts
            * Whether to repeat for all 3 days (e.g. bar will have different opening hours based on day)
        + Individually
    - With:
        + A role (e.g. 'A/V')
        + A venue (e.g. 'Stage A')
        + Start time
        + A hand-over period (a shift should probably start 15min before the previous shift is supposed to end to allow proper handover of information and so we have time to find replacements for no-shows)
        + A description box (to include links on 'how-to' as well as useful numbers etc.)
* Have the opportunity to preview any changes made to shifts before confirming them.

> Need to look at how we're going to create data. `apps/volunteer/tasks.py` has `make_shifts` CLI command. I don't think that matches what was done last time (camera operator and vision mixer weren't handled in volunteer system) and is only for things tied to a proposal in the schedule. There is also `Shift.generate_for()`, but only looks to be used in dev task to set up dummy data. 

It would be nice to have:
-------------------------
* Schedule integration
* APIs for:
    - Individual's alerts
    - General alerts
    - The data set
