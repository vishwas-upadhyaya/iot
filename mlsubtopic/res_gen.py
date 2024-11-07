import cohere

# Set up the API key
co = cohere.Client('nGWy1B5vIORpuiK5jpbys1cSSrWHAiR8thjeQnew')

def get_text(prompt):
    # co = cohere.Client('nGWy1B5vIORpuiK5jpbys1cSSrWHAiR8thjeQnew')

    # Generate a response
    # prompt = """Generate crisp summary for - In Hindu astrology, seeing a dead snake is important because it means big changes
    # are coming. It's like a sign that says the tough times are ending and better days are ahead, where you'll learn
    # a lot and become a better person. Snakes are special in these beliefs; they're seen as very wise and powerful."
    # In Hindu astrology, if you see a dead snake, it means that big changes are coming soon in your life. These changes
    # will be for the better, where you will learn a lot and become a better person afterward. Snakes are seen as wise
    # and powerful in these beliefs, so this vision bears a special significance. In Hindu astrology, if you see a dead snake, it means that you will undergo significant changes in your life.
    # These changes will be indicative of growth and transformation. You will learn new things about yourself and
    # become wiser as a result. Snakes are considered to be especially wise and powerful in these traditions, so
    # witnessing one represents a symbolic renewal and a reminder of their innate wisdom."""
    prompt = "make the brief summary for the quoted texts \" " + prompt + " \""
    response = co.generate(
    model='command',
    prompt=prompt,
    # max_tokens=100,
    temperature=0.5)


# Print the generated text
#     del co
    return response.generations[0].text
    # print(response.generations[0].text)

# Generate crisp summary for - In Hindu astrology, seeing a dead snake is important because it means big changes
# are coming. It's like a sign that says the tough times are ending and better days are ahead, where you'll learn
# a lot and become a better person. Snakes are special in these beliefs; they're seen as very wise and powerful."
# In Hindu astrology, if you see a dead snake, it means that big changes are coming soon in your life. These changes
# will be for the better, where you will learn a lot and become a better person afterward. Snakes are seen as wise
# and powerful in these beliefs, so this vision bears a special significance. In Hindu astrology, if you see a dead snake,
# it means that you will undergo significant changes in your life.
# These changes will be indicative of growth and transformation. You will learn new things about yourself and
# become wiser as a result. Snakes are considered to be especially wise and powerful in these traditions, so
# witnessing one represents a symbolic renewal and a reminder of their innate wisdom.



# In the astrological tradition of Hinduism, seeing a dead snake signifies that significant changes are about to occur
# in your life, and these changes will bring about growth and transformation. It is believed that you will gain new
# insights about yourself and become wiser as a result. Snakes are regarded as especially wise and powerful in Hindu
# tradition, so encountering a dead snake represents symbolic renewal and a reminder of one's own wisdom.

