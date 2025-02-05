def calculate_love_score(name1, name2):
    # Combine the names and convert to lowercase for consistent counting
    combined_names = (name1 + name2).lower()
    
    # Count occurrences of letters in "TRUE"
    true_count = (combined_names.count("t") +
                  combined_names.count("r") +
                  combined_names.count("u") +
                  combined_names.count("e"))
    
    # Count occurrences of letters in "LOVE"
    love_count = (combined_names.count("l") +
                  combined_names.count("o") +
                  combined_names.count("v") +
                  combined_names.count("e"))
    
    # Combine the counts to form a two-digit number
    love_score = int(str(true_count) + str(love_count))
    
    # Print the love score
    print(love_score)

# Example call with hard-coded values
calculate_love_score("Kanye West", "Kim Kardashian")

