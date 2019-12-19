import discord
import random
import datetime
import R6S
client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("명령어 적기 귀찮아")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith('/레식 방어팀 추천'):
        Sube =['예비', '스모크', '뮤트', '캐슬', '펄스', '닥', '룩', '캅칸', '타찬카', '예거', '밴딧', '프로스트', '발키리', '카베이라', '에코', '미라', '리전', '엘라', '비질', '마에스트로', '알리바이', '클래쉬', '카이드', '모찌', '워든', '고요', '와마이']
        await message.channel.send(random.choice(Sube))

    if message.content.startswith('/내정보'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.set_author(name=client.user.name)
        embed.add_field(name="이름", value=message.author.name, inline=False)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=False)
        embed.add_field(name="가입일", value=str(date.year)+'년  '+str(date.month)+'월  '+str(date.day)+'일  ', inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_footer(text="Bot Made.Simli")
        await message.channel.send(embed=embed)
    if message.content.startswith('/레식전적test'):
        user_name = message.content.split(" ")[1]
        total_kill = R6S.Total_kill(user_name)
        total_death = R6S.Total_death(user_name)
        embed = discord.Embed(color=0x00ff00)
        embed.set_author(name = user_name+' 님의 전적test')
        embed.add_field(name='킬 / kill', value=total_kill)
        embed.add_field(name='데스 / death', value=total_death)
        embed.set_footer(text='Bot Made.Simli')
        await message.channel.send(embed=embed)
    if message.content.startswith('/예정추가내용'):
        await message.channel.send('팀 나누기')
client.run('NjUyODE2OTYwNTgwNjE2MjI1.Xet9eg.-tJRnXJdWGhioNJmrbdz6kcRrbs')