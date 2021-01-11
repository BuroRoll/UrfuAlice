# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = welcome_from_dict(json.loads(json_string))

from typing import Optional, Any, Dict, TypeVar, Type, Callable, cast
from datetime import datetime
import dateutil.parser


T = TypeVar("T")


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class GroupInfo:
    sgroup_id: Optional[int]
    sgroup_external_id: None
    sgroup_uuid: Optional[str]
    sgroup_name: Optional[str]
    sgroup_course: Optional[int]
    sgroup_division: None
    sgroup_eduyear: None
    sgroup_pkey: None
    sspec_id: Optional[int]
    sgroup_start_education_year: Optional[int]
    sgroup_date_add: Optional[datetime]
    sgroup_date_modified: Optional[datetime]
    sgroup_its_group_id: None
    sgroup_its_group_type_id: None
    sgroup_its_group_key: None
    sspec_code_okso: Optional[str]
    sspec_title: Optional[str]

    def __init__(self, sgroup_id: Optional[int], sgroup_external_id: None, sgroup_uuid: Optional[str], sgroup_name: Optional[str], sgroup_course: Optional[int], sgroup_division: None, sgroup_eduyear: None, sgroup_pkey: None, sspec_id: Optional[int], sgroup_start_education_year: Optional[int], sgroup_date_add: Optional[datetime], sgroup_date_modified: Optional[datetime], sgroup_its_group_id: None, sgroup_its_group_type_id: None, sgroup_its_group_key: None, sspec_code_okso: Optional[str], sspec_title: Optional[str]) -> None:
        self.sgroup_id = sgroup_id
        self.sgroup_external_id = sgroup_external_id
        self.sgroup_uuid = sgroup_uuid
        self.sgroup_name = sgroup_name
        self.sgroup_course = sgroup_course
        self.sgroup_division = sgroup_division
        self.sgroup_eduyear = sgroup_eduyear
        self.sgroup_pkey = sgroup_pkey
        self.sspec_id = sspec_id
        self.sgroup_start_education_year = sgroup_start_education_year
        self.sgroup_date_add = sgroup_date_add
        self.sgroup_date_modified = sgroup_date_modified
        self.sgroup_its_group_id = sgroup_its_group_id
        self.sgroup_its_group_type_id = sgroup_its_group_type_id
        self.sgroup_its_group_key = sgroup_its_group_key
        self.sspec_code_okso = sspec_code_okso
        self.sspec_title = sspec_title

    @staticmethod
    def from_dict(obj: Any) -> 'GroupInfo':
        assert isinstance(obj, dict)
        sgroup_id = from_union([from_none, lambda x: int(from_str(x))], obj.get("sgroup_id"))
        sgroup_external_id = from_none(obj.get("sgroup_external_id"))
        sgroup_uuid = from_union([from_str, from_none], obj.get("sgroup_uuid"))
        sgroup_name = from_union([from_str, from_none], obj.get("sgroup_name"))
        sgroup_course = from_union([from_none, lambda x: int(from_str(x))], obj.get("sgroup_course"))
        sgroup_division = from_none(obj.get("sgroup_division"))
        sgroup_eduyear = from_none(obj.get("sgroup_eduyear"))
        sgroup_pkey = from_none(obj.get("sgroup_pkey"))
        sspec_id = from_union([from_none, lambda x: int(from_str(x))], obj.get("sspec_id"))
        sgroup_start_education_year = from_union([from_none, lambda x: int(from_str(x))], obj.get("sgroup_start_education_year"))
        sgroup_date_add = from_union([from_datetime, from_none], obj.get("sgroup_date_add"))
        sgroup_date_modified = from_union([from_datetime, from_none], obj.get("sgroup_date_modified"))
        sgroup_its_group_id = from_none(obj.get("sgroup_its_group_id"))
        sgroup_its_group_type_id = from_none(obj.get("sgroup_its_group_type_id"))
        sgroup_its_group_key = from_none(obj.get("sgroup_its_group_key"))
        sspec_code_okso = from_union([from_str, from_none], obj.get("sspec_code_okso"))
        sspec_title = from_union([from_str, from_none], obj.get("sspec_title"))
        return GroupInfo(sgroup_id, sgroup_external_id, sgroup_uuid, sgroup_name, sgroup_course, sgroup_division, sgroup_eduyear, sgroup_pkey, sspec_id, sgroup_start_education_year, sgroup_date_add, sgroup_date_modified, sgroup_its_group_id, sgroup_its_group_type_id, sgroup_its_group_key, sspec_code_okso, sspec_title)

    def to_dict(self) -> dict:
        result: dict = {}
        result["sgroup_id"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.sgroup_id)
        result["sgroup_external_id"] = from_none(self.sgroup_external_id)
        result["sgroup_uuid"] = from_union([from_str, from_none], self.sgroup_uuid)
        result["sgroup_name"] = from_union([from_str, from_none], self.sgroup_name)
        result["sgroup_course"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.sgroup_course)
        result["sgroup_division"] = from_none(self.sgroup_division)
        result["sgroup_eduyear"] = from_none(self.sgroup_eduyear)
        result["sgroup_pkey"] = from_none(self.sgroup_pkey)
        result["sspec_id"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.sspec_id)
        result["sgroup_start_education_year"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.sgroup_start_education_year)
        result["sgroup_date_add"] = from_union([lambda x: x.isoformat(), from_none], self.sgroup_date_add)
        result["sgroup_date_modified"] = from_union([lambda x: x.isoformat(), from_none], self.sgroup_date_modified)
        result["sgroup_its_group_id"] = from_none(self.sgroup_its_group_id)
        result["sgroup_its_group_type_id"] = from_none(self.sgroup_its_group_type_id)
        result["sgroup_its_group_key"] = from_none(self.sgroup_its_group_key)
        result["sspec_code_okso"] = from_union([from_str, from_none], self.sspec_code_okso)
        result["sspec_title"] = from_union([from_str, from_none], self.sspec_title)
        return result


class Event:
    ntk: Optional[bool]
    loadcase: Optional[str]
    retake: Optional[bool]
    event_date: Optional[int]
    begin_time: Optional[str]
    end_time: Optional[str]
    npair: Optional[int]
    nday: None
    teacher: Optional[str]
    teacher_auditory: None
    teacher_auditory_location: None
    teacher_auditory_capacity: None
    auditory: Optional[str]
    auditory_location: Optional[str]
    auditory_capacity: Optional[int]
    comment: Optional[str]
    distations: Optional[bool]
    ntk_retake: Optional[bool]
    teachers_comment: None
    teachers_link: None
    auditory_location_is_link: Optional[int]
    teacher_auditory_location_is_link: Optional[int]
    loadtype: Optional[str]
    discipline: Optional[str]
    state: Optional[str]
    teachers_comment_exists: Optional[bool]

    def __init__(self, ntk: Optional[bool], loadcase: Optional[str], retake: Optional[bool], event_date: Optional[int], begin_time: Optional[str], end_time: Optional[str], npair: Optional[int], nday: None, teacher: Optional[str], teacher_auditory: None, teacher_auditory_location: None, teacher_auditory_capacity: None, auditory: Optional[str], auditory_location: Optional[str], auditory_capacity: Optional[int], comment: Optional[str], distations: Optional[bool], ntk_retake: Optional[bool], teachers_comment: None, teachers_link: None, auditory_location_is_link: Optional[int], teacher_auditory_location_is_link: Optional[int], loadtype: Optional[str], discipline: Optional[str], state: Optional[str], teachers_comment_exists: Optional[bool]) -> None:
        self.ntk = ntk
        self.loadcase = loadcase
        self.retake = retake
        self.event_date = event_date
        self.begin_time = begin_time
        self.end_time = end_time
        self.npair = npair
        self.nday = nday
        self.teacher = teacher
        self.teacher_auditory = teacher_auditory
        self.teacher_auditory_location = teacher_auditory_location
        self.teacher_auditory_capacity = teacher_auditory_capacity
        self.auditory = auditory
        self.auditory_location = auditory_location
        self.auditory_capacity = auditory_capacity
        self.comment = comment
        self.distations = distations
        self.ntk_retake = ntk_retake
        self.teachers_comment = teachers_comment
        self.teachers_link = teachers_link
        self.auditory_location_is_link = auditory_location_is_link
        self.teacher_auditory_location_is_link = teacher_auditory_location_is_link
        self.loadtype = loadtype
        self.discipline = discipline
        self.state = state
        self.teachers_comment_exists = teachers_comment_exists

    @staticmethod
    def from_dict(obj: Any) -> 'Event':
        assert isinstance(obj, dict)
        ntk = from_union([from_bool, from_none], obj.get("ntk"))
        loadcase = from_union([from_none, from_str], obj.get("loadcase"))
        retake = from_union([from_bool, from_none], obj.get("retake"))
        event_date = from_union([from_int, from_none], obj.get("event_date"))
        begin_time = from_union([from_str, from_none], obj.get("begin_time"))
        end_time = from_union([from_str, from_none], obj.get("end_time"))
        npair = from_union([from_int, from_none], obj.get("npair"))
        nday = from_none(obj.get("nday"))
        teacher = from_union([from_none, from_str], obj.get("teacher"))
        teacher_auditory = from_none(obj.get("teacher_auditory"))
        teacher_auditory_location = from_none(obj.get("teacher_auditory_location"))
        teacher_auditory_capacity = from_none(obj.get("teacher_auditory_capacity"))
        auditory = from_union([from_none, from_str], obj.get("auditory"))
        auditory_location = from_union([from_none, from_str], obj.get("auditory_location"))
        auditory_capacity = from_union([from_int, from_none], obj.get("auditory_capacity"))
        comment = from_union([from_str, from_none], obj.get("comment"))
        distations = from_union([from_bool, from_none], obj.get("distations"))
        ntk_retake = from_union([from_bool, from_none], obj.get("ntk_retake"))
        teachers_comment = from_none(obj.get("teachers_comment"))
        teachers_link = from_none(obj.get("teachers_link"))
        auditory_location_is_link = from_union([from_int, from_none], obj.get("auditory_location_is_link"))
        teacher_auditory_location_is_link = from_union([from_int, from_none], obj.get("teacher_auditory_location_is_link"))
        loadtype = from_union([from_str, from_none], obj.get("loadtype"))
        discipline = from_union([from_str, from_none], obj.get("discipline"))
        state = from_union([from_str, from_none], obj.get("state"))
        teachers_comment_exists = from_union([from_bool, from_none], obj.get("teachers_comment_exists"))
        return Event(ntk, loadcase, retake, event_date, begin_time, end_time, npair, nday, teacher, teacher_auditory, teacher_auditory_location, teacher_auditory_capacity, auditory, auditory_location, auditory_capacity, comment, distations, ntk_retake, teachers_comment, teachers_link, auditory_location_is_link, teacher_auditory_location_is_link, loadtype, discipline, state, teachers_comment_exists)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ntk"] = from_union([from_bool, from_none], self.ntk)
        result["loadcase"] = from_union([from_none, from_str], self.loadcase)
        result["retake"] = from_union([from_bool, from_none], self.retake)
        result["event_date"] = from_union([from_int, from_none], self.event_date)
        result["begin_time"] = from_union([from_str, from_none], self.begin_time)
        result["end_time"] = from_union([from_str, from_none], self.end_time)
        result["npair"] = from_union([from_int, from_none], self.npair)
        result["nday"] = from_none(self.nday)
        result["teacher"] = from_union([from_none, from_str], self.teacher)
        result["teacher_auditory"] = from_none(self.teacher_auditory)
        result["teacher_auditory_location"] = from_none(self.teacher_auditory_location)
        result["teacher_auditory_capacity"] = from_none(self.teacher_auditory_capacity)
        result["auditory"] = from_union([from_none, from_str], self.auditory)
        result["auditory_location"] = from_union([from_none, from_str], self.auditory_location)
        result["auditory_capacity"] = from_union([from_int, from_none], self.auditory_capacity)
        result["comment"] = from_union([from_str, from_none], self.comment)
        result["distations"] = from_union([from_bool, from_none], self.distations)
        result["ntk_retake"] = from_union([from_bool, from_none], self.ntk_retake)
        result["teachers_comment"] = from_none(self.teachers_comment)
        result["teachers_link"] = from_none(self.teachers_link)
        result["auditory_location_is_link"] = from_union([from_int, from_none], self.auditory_location_is_link)
        result["teacher_auditory_location_is_link"] = from_union([from_int, from_none], self.teacher_auditory_location_is_link)
        result["loadtype"] = from_union([from_str, from_none], self.loadtype)
        result["discipline"] = from_union([from_str, from_none], self.discipline)
        result["state"] = from_union([from_str, from_none], self.state)
        result["teachers_comment_exists"] = from_union([from_bool, from_none], self.teachers_comment_exists)
        return result


class Schedule:
    event_date: Optional[int]
    events: Optional[Dict[str, Event]]

    def __init__(self, event_date: Optional[int], events: Optional[Dict[str, Event]]) -> None:
        self.event_date = event_date
        self.events = events

    @staticmethod
    def from_dict(obj: Any) -> 'Schedule':
        assert isinstance(obj, dict)
        event_date = from_union([from_int, from_none], obj.get("event_date"))
        events = from_union([lambda x: from_dict(Event.from_dict, x), from_none], obj.get("events"))
        return Schedule(event_date, events)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_date"] = from_union([from_int, from_none], self.event_date)
        result["events"] = from_union([lambda x: from_dict(lambda x: to_class(Event, x), x), from_none], self.events)
        return result


class Welcome:
    schedule: Optional[Dict[str, Schedule]]
    i_cal: Optional[str]
    group_info: Optional[GroupInfo]
    today: Optional[int]
    start_date: Optional[int]
    end_date: Optional[int]
    prev_start_date: Optional[int]
    next_start_date: Optional[int]

    def __init__(self, schedule: Optional[Dict[str, Schedule]], i_cal: Optional[str], group_info: Optional[GroupInfo], today: Optional[int], start_date: Optional[int], end_date: Optional[int], prev_start_date: Optional[int], next_start_date: Optional[int]) -> None:
        self.schedule = schedule
        self.i_cal = i_cal
        self.group_info = group_info
        self.today = today
        self.start_date = start_date
        self.end_date = end_date
        self.prev_start_date = prev_start_date
        self.next_start_date = next_start_date

    @staticmethod
    def from_dict(obj: Any) -> 'Welcome':
        assert isinstance(obj, dict)
        schedule = from_union([lambda x: from_dict(Schedule.from_dict, x), from_none], obj.get("schedule"))
        i_cal = from_union([from_str, from_none], obj.get("iCal"))
        group_info = from_union([GroupInfo.from_dict, from_none], obj.get("groupInfo"))
        today = from_union([from_int, from_none], obj.get("today"))
        start_date = from_union([from_int, from_none], obj.get("start_date"))
        end_date = from_union([from_int, from_none], obj.get("end_date"))
        prev_start_date = from_union([from_int, from_none], obj.get("prev_start_date"))
        next_start_date = from_union([from_int, from_none], obj.get("next_start_date"))
        return Welcome(schedule, i_cal, group_info, today, start_date, end_date, prev_start_date, next_start_date)

    def to_dict(self) -> dict:
        result: dict = {}
        result["schedule"] = from_union([lambda x: from_dict(lambda x: to_class(Schedule, x), x), from_none], self.schedule)
        result["iCal"] = from_union([from_str, from_none], self.i_cal)
        result["groupInfo"] = from_union([lambda x: to_class(GroupInfo, x), from_none], self.group_info)
        result["today"] = from_union([from_int, from_none], self.today)
        result["start_date"] = from_union([from_int, from_none], self.start_date)
        result["end_date"] = from_union([from_int, from_none], self.end_date)
        result["prev_start_date"] = from_union([from_int, from_none], self.prev_start_date)
        result["next_start_date"] = from_union([from_int, from_none], self.next_start_date)
        return result


def welcome_from_dict(s: Any) -> Welcome:
    return Welcome.from_dict(s)


def welcome_to_dict(x: Welcome) -> Any:
    return to_class(Welcome, x)
