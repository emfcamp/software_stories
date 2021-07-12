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
>> JW: Pretty sure this never got used except for the bar.

## Availability
Allow volunteers to indicate that they don't mind the specific role they perform.

* Free shift - The volunteer indicates that they are happy to be assigned any (normal) shift they are trained to do.
* Cover - the volunteer indicates that they are happy to be contacted to fill required shifts if need be.

> Thinking to cover this with new role (runner?) giving pool of people to 
> * provide cover where other shifts are short
> * Do one off tasks
> * Do recurring tasks/checks

>> JW: I think a runner role is a good thing to have, but isn't the same as allowing people to express that they're
>> happy to volunteer for [insert list of roles] and don't have strong opinions as to when or where they do that.

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
  >> JW: Probably role/signed up shifts/schedule are the only filters that actually matter. "Needed now" might be nice
  >> if people find themselves available and willing to fill a shift.
  
  > Currently hardcoded Fri/Sat/Sun/Mon, which is active (when not in URL arg) is from current day of the week, could possibly do with a check for date being during event for that?
  
  > Don't have filters? There is a `filter-panel` in the template should some js be populating it?
  
  > Lists all shifts without filtering by which roles user is interested/trained in?
  
  > Links to other days in tab content don't work
  
  > Possibly a lot of this is from JS not running? https://github.com/emfcamp/Website/issues/868#issuecomment-586746500
  
  > Would be nice to have schedule show shifts you're signed up for - currently "Sign Up" button would become a "Cancel" button, is that enough?
  >> JW: I think this already exists.
  
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
    > I don't think there are any automatic notifications? Manually sent emails discussed below in manager section. 
    
    > Do we want automatic notifications? Would need to properly flesh out opting in for them in sign up flow, opting out later etc. 
* Be able to change my notification settings
* Be able to communicate with managers and/or an admin
* Provide extra information
    - Phone number
    > Phone number is currently required to sign up as a volunteer (though there is no check that the number given is real). I'd like to remove that requirement. I'm thinking email address as only required contact details and optional fields for phone number (for public and eventphone system), IRC nick or other contact details. 
    >> JW: +1 to a more freeform "how to contact me" field unless we actually do SMS notifications
    - Age
    - Misc details (e.g. experience)
* When on shift
    - Log that my replacement has not arrived on time (if unmanaged)
    - Request help at any time
    - Have access to information about the role
    > I don't think we have anything for these at the moment. I'm not sure about putting first two in system - rather they are just "contact volunteer desk"
    
    > Info about the role is something I'd like to improve. Previously a lot of the what you're actually doing on a shift was passed from volunteer to volunteer in a pretty ad hoc way. I'd like to get complete instructions in the system, and have some way to add/change that as we figure out more during the event. Possibly just have wiki page for instructions for each role? Allow anyone to edit them? Can have volunteer manager(s) watching the pages so they get emails on changes and can revert anything that's obviously wrong/vandalism. 
    >> JW: Role details are currently baked in as static files - definitely better to be able to link to a wiki page which people can edit over time to 
    >> provide more detail on what's involved.
    
* Change a shift
    - And be alerted if doing so will flag me as a no-show for that shift (i.e. if I try to change a shift within 15 min of its start)
  > Looks like there is processing to cancel doing a shift (button on sign up page toggles if you're signed up for the shift or not) but nothing to check time is far enough before start. I'd like some kind of notification to volunteer manager if shift is cancelled "close" to start. 

> Currently default page for `/volunteer/` (what's linked from main site nav bar) is `/volunteer/account` probably better to make that be `/volunteer/schedule` after they've signed up. Can change that in `sign_up.py` L77 change to `redirect(url_for(".schedule"))` Do we want something else here for before the event? Are we going to allow signing up to volunteer system (and shifts) before event? I'm inclined towards: yes allowing people to sign up. 

As a trainer I would like to:
-----------------------------
* Approve a volunteer as trained for a role
* Sign up to train a training session (?)

> Marking people as trained is handled in `apps/volunteer/training.py` 

> Requires volunteer admin privileges

> Is pretty clunky - just shows list of all volunteers who're interested in role with checkbox for trained. 

> I think tracking training in volunteer system was only done for bar previously and it was auto ticked when they completed questions so this UI was never actually used. Is it going to be needed this time or are we likely to only need training for bar and it'll auto mark people as trained?

>> JW: +1 - I doubt this would be used in practice.

As a manager I would like to:
-----------------------------

> I don't think we have a role manager so most of this functionality is folded into volunteer admin. 

* Assign free volunteers to shifts
* Change who's on a shift (with and without flagging them as a no-show)
* Edit shift info
* Mark whether a volunteer attended their shift

> JW: I don't see this getting used in practice, presumably it would be team leads responsible for
> updating this, and they've already got enough to do without also ticking boxes to say whether people
> turned up. What would happen if someone doesn't turn up?

* Respond to questions/concerns of volunteers
* Ban a volunteer (and record a reason) from
    - A role
    - All roles
  > We have a `Banned` boolean attached to a user but no provision for giving a reason, or it being only for some roles. Not sure if that is checked anywhere?
  >> JW: I'm not at all clear what the use case is for banning a volunteer - if someone has done something heinous enough to get banned from volunteering
  >> they should probably just be asked to leave.
  
* View all volunteers that have signed up for a session
* Contact:
    - All volunteers
    - All volunteers with certain training
    - All volunteers who have signed up for a free shift
    - All volunteers who have indicated that they may do cover shifts
  > There is option to manually send email to volunteers at `notifications/emailvolunteers`
    
  > Currently broken with `notification/base.html` using `{% assets %}`. I've commented that out to be able to poke at it (without CSS) but need to fix it properly. Related: https://github.com/emfcamp/Website/issues/869
    
  > Currently only offers option to email all users interested in a role. Would really like to be able to send message to a subset of them (with some shuffling/tracking so it isn't always the same subset). Can then figure out how many people we should be mailing for the number we need to get. 
  
  > Would like to be able to email all volunteers signed up for particular shift(s) if there are changes or other info we need to ping them. 
  
  > Isn't limited to users who've checked `allow_comms_during_event`?

  >> JW: Again, not sure what the use case is in practice - maybe others are different, but if you need to get time sensitive information to me email
  >> isn't the way to do it. This needs to go via a more immediate channel to be useful.

* View which volunteers are currently in which shifts
  > I think this will be  visible on `volunteer/shift/<id>`. Page has a "These people are on this shift" bit. But getting to there is only possible from schedule? 
* View which current shifts require volunteers
* View which upcoming shifts require volunteers
  > `volunteer/schedule` shows count of signed up over needed. 
  >> JW: The volunteer schedule overview for managers could do with a ton of work on it's UI to make it useful.


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
