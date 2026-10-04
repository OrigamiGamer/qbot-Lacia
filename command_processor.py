import user_database


def process_command(uid: str, full_command: str) -> str:
    if len(full_command) > 0:
        while full_command[0] == " ":
            full_command = full_command.removeprefix(" ")
    cmds: list[str] = full_command.split(" ")
    if len(cmds) == 0 and str != "":
        cmds.append(full_command)

    # command blocks
    # TODO: better parser of command blocks
    cmd: str = cmds[0]
    params: list[str] = cmds
    params.pop(0)
    count_param = len(params)

    if cmd != "":
        # 用户信息
        # /info
        if cmd == "/info":
            if count_param == 0:
                info = (
                    "\n"
                    + "用户名称: "
                    + user_database.get_user_info(uid, "name")
                    + "\n"
                )
                info += "权限等级: " + user_database.get_user_info(uid, "permission_level")
                return info
            return ""
        # 设置
        if cmd == "/set" and count_param:
            # /set info -name <username>
            return ""
    return ""
