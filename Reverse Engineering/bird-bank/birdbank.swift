class BirdBank {
  func chr(_ value: Int) -> Character? {
      return UnicodeScalar(value).map { Character($0) }
  }

  func ord(_ character: Character) -> Int? {
      guard let unicodeScalar = character.unicodeScalars.first else {
          return nil
      }
      return Int(unicodeScalar.value)
  }

  func birdbank(word: String) -> String {
      var ret = ""
      let wordArray = Array(word)

      for value in 0...wordArray.count - 1 {
          if value % 2 == 0 {
              ret.append(chr((ord(wordArray[value]) ?? 0) - 3) ?? " ")
          } else if (ord(wordArray[value]) == 125) || (ord(wordArray[value]) == 124) {
              ret.append(chr((ord(wordArray[value]) ?? 0) - 2) ?? " ")
          } else {
              ret.append(chr((ord(wordArray[value]) ?? 0) - 1) ?? " ")
          }
      }

      return ret
  }
  // goofy and funky Swift rule: Because "\" is used to escape characters, "\" is represented with "\\"
  func main() -> Void {
      let flag = "qdoqlq@SCz.l\\c1^_0df0rq^_0ocz"
      print("Welcome to the Bird Bank!")
      print("Enter your passkey: ", terminator: "")
      let attempt = readLine()
      let encattempt = birdbank(word: attempt!)
      if encattempt == flag {
          print("Access granted!")
      } else {
          print("Access denied!")
      }
  }
}

let birdBankInstance = BirdBank()
birdBankInstance.main()
