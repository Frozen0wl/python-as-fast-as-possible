import json
data = ""
with open("example_2.json", "r") as f:
    data = json.load(f)



with open("example_2.json", "w") as f:
    data["quiz"]["sport"]["q1"]["options"].append("test")
    json.dump(data, f, indent = 4)


async def addtoblacklist(self, ctx, member: discord.Member):
        data = None
        try:
            with open("blacklist.json", "r") as f:
                data = json.load(f)
            with open("blacklist.json", "w") as f:
                data.append(member.id)
        except FileNotFoundError:
            with open("blacklist.json", "w") as f:
                pass
        await ctx.send(f"{member} added to the blacklist")

