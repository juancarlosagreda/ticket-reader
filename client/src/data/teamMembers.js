
import { faCalendarCheck, faComment } from '@fortawesome/free-solid-svg-icons';

import Profile1 from "../assets/img/team/default-profile.jpg"
import Profile2 from "../assets/img/team/default-profile.jpg"
import Profile3 from "../assets/img/team/default-profile.jpg"
import Profile4 from "../assets/img/team/default-profile.jpg"

export default [
    {
        "id": 1,
        "image": Profile1,
        "name": "Fernando Carazo",
        "statusKey": "online",
        "icon": faCalendarCheck,
        "btnText": "Invite"
    },
    {
        "id": 2,
        "image": Profile2,
        "name": "Alfredo Artiles",
        "statusKey": "inMeeting",
        "icon": faComment,
        "btnText": "Message"
    },
    {
        "id": 3,
        "image": Profile3,
        "name": "Juan Carlos Agreda",
        "statusKey": "offline",
        "icon": faCalendarCheck,
        "btnText": "Invite"
    },
    {
        "id": 4,
        "image": Profile4,
        "name": "Miguel Burguete",
        "statusKey": "online",
        "icon": faComment,
        "btnText": "Message"
    }
]